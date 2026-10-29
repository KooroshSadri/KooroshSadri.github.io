#!/usr/bin/env python3
"""Check links, assets, and HTML fragments in a built Jekyll site.

Usage: python tools/check_links.py _site --report ../qa/links.json
Optional --external checks public URLs with bounded GET requests. HTTP 403/429,
timeouts and server failures are reported as unverifiable, not broken links.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen


class Page(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "a" and values.get("name"):
            self.ids.add(values["name"])
        for key in ("href", "src", "poster", "action", "data-src", "data-href"):
            if values.get(key):
                self.references.append((f"{tag}[{key}]", values[key]))
        if tag == "object" and values.get("data"):
            self.references.append(("object[data]", values["data"]))
        if values.get("srcset"):
            for part in values["srcset"].split(","):
                target = part.strip().split()[0] if part.strip() else ""
                if target:
                    self.references.append((f"{tag}[srcset]", target))
        for target in re.findall(r"url\(\s*['\"]?([^)'\"]+)", values.get("style", "")):
            self.references.append((f"{tag}[style]", target.strip()))


def page_url(relative: Path) -> str:
    name = relative.as_posix()
    return "/" + (name[:-10] if name.endswith("index.html") else name)


def resolve_target(root: Path, path: str):
    candidate = root.joinpath(unquote(path).lstrip("/")).resolve()
    if not candidate.is_relative_to(root):
        return None
    choices = [candidate]
    if candidate.is_dir() or path.endswith("/"):
        choices.append(candidate / "index.html")
    else:
        choices.extend([candidate.with_suffix(candidate.suffix + ".html"), candidate / "index.html"])
    return next((item for item in choices if item.is_file()), None)


def external_status(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; PersonalSiteLinkCheck/1.0)", "Range": "bytes=0-4095"})
    try:
        with urlopen(request, timeout=20) as response:
            response.read(4096)
            error_redirect = re.search(r"/(?:errors?/)?(403|404|410)(?:[./]|$)", urlsplit(response.url).path)
            result = "ok"
            if error_redirect:
                result = "broken" if error_redirect.group(1) in ("404", "410") else "unverified"
            return {"url": url, "status": response.status, "final_url": response.url, "result": result}
    except HTTPError as error:
        return {"url": url, "status": error.code, "final_url": error.url,
                "result": "broken" if error.code in (404, 410) else "unverified"}
    except (URLError, TimeoutError, OSError) as error:
        return {"url": url, "result": "unverified", "error": str(error)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--site-url", default="https://kooroshsadri.github.io")
    parser.add_argument("--external", action="store_true")
    parser.add_argument("--strict-external", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = args.directory.resolve()
    if not (root / "index.html").is_file():
        parser.error(f"No built homepage found in {root}")
    host = urlsplit(args.site_url).netloc.lower()
    pages = {}
    refs = []
    for path in sorted(root.rglob("*.html")):
        pages[path] = Page(path.read_text(encoding="utf-8", errors="replace"))
        refs.extend((path, kind, target) for kind, target in pages[path].references)
    for path in sorted(root.rglob("*.css")):
        css = re.sub(r"/\*.*?\*/", "", path.read_text(encoding="utf-8", errors="replace"), flags=re.S)
        refs.extend((path, "css[url]", target.strip()) for target in re.findall(r"url\(\s*['\"]?([^)'\"]+)", css))
    errors, external = [], {}
    checked = 0
    for origin, kind, target in refs:
        if target.startswith(("data:", "mailto:", "tel:", "javascript:", "blob:")) or target == "#":
            continue
        relative = origin.relative_to(root)
        base = args.site_url.rstrip("/") + page_url(relative)
        absolute = urljoin(base, target)
        parsed = urlsplit(absolute)
        if parsed.scheme not in ("http", "https"):
            continue
        if parsed.netloc.lower() != host:
            external_url = urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, ""))
            external.setdefault(external_url, []).append(relative.as_posix())
            continue
        checked += 1
        resolved = resolve_target(root, parsed.path)
        issue = {"page": relative.as_posix(), "kind": kind, "target": target}
        if resolved is None:
            errors.append({**issue, "error": "missing target", "resolved_path": parsed.path})
        elif parsed.fragment and resolved.suffix.lower() == ".html" and not parsed.fragment.startswith(":~:text="):
            parsed_page = pages.get(resolved)
            if parsed_page and unquote(parsed.fragment) not in parsed_page.ids:
                errors.append({**issue, "error": "missing fragment", "fragment": unquote(parsed.fragment)})
    results = []
    if args.external:
        with ThreadPoolExecutor(max_workers=6) as workers:
            results = list(workers.map(external_status, sorted(external)))
        for result in results:
            result["pages"] = sorted(set(external[result["url"]]))
    report = {"html_pages": len(pages), "internal_references_checked": checked,
              "internal_errors": errors, "external_url_count": len(external),
              "external_urls": sorted(external), "external_results": results}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"HTML pages: {len(pages)}; internal references: {checked}; internal errors: {len(errors)}")
    for issue in errors:
        print(f"ERROR {issue['page']}: {issue['target']} ({issue['error']})")
    if args.external:
        for result in results:
            if result["result"] != "ok":
                print(f"{result['result'].upper()} {result['url']}: {result.get('status', result.get('error'))}")
        print(f"External URLs: {len(results)}; OK: {sum(r['result'] == 'ok' for r in results)}; "
              f"broken: {sum(r['result'] == 'broken' for r in results)}; "
              f"unverified: {sum(r['result'] == 'unverified' for r in results)}")
    raise SystemExit(1 if errors or (args.strict_external and any(r["result"] == "broken" for r in results)) else 0)


if __name__ == "__main__":
    main()
