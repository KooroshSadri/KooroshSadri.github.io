# Koorosh Sadri's website

A simple Jekyll website for GitHub Pages. Dark mode is the default; the theme button remembers each visitor's choice.

## Replace the current site

1. Keep a backup of the current repository.
2. Replace the old website contents with this folder's contents, removing obsolete source files too. Preserve your local `.git` folder. `_config.yml` must be at the repository root, not inside an extra folder; include `.gitignore`.
3. Commit and push the replacement to the branch used by GitHub Pages. Keep Pages publishing from that branch's root folder.
4. Wait for the Pages deployment to finish, then check the homepage, Research, CV, and a Notes PDF.

The package contains source files. Do not upload a generated `_site` folder. No deployment has been performed for you.

## Edit the homepage or navigation

Edit the introduction in `_pages/about.md`, the sidebar in `_config.yml`, and the menu in `_data/navigation.yml`. Research and the blog are separate. The old `/publications/` address redirects to Research.

## Publish a blog post

Copy `_drafts/example-post.md` into `_posts/`, naming it `YYYY-MM-DD-short-title.md`. Replace the title, excerpt, and body, and use the intended publication date. Posts appear on the homepage, newest first. Drafts and future-dated posts remain unpublished.

Markdown, mathematical notation, and YouTube iframe embeds are supported. The example draft includes brief instructions.

## Add a research item

Copy an existing file in `_research/` to a new filename. Update its title, summary, explanatory text, and `publications` list. Each publication has a `title`, `citation`, `scholar_url`, and an `authors` list of full names. The project automatically combines those author lists without duplicates and displays Koorosh Sadri as bold **KS**.

Use a numeric `year` for the project's final year and an optional `start_year` for a range: `start_year: 2023` with `year: 2025` displays **2023–2025**. Projects are sorted by their final year, newest first. Publication dates in the citations can differ from the project dates. Each publication title links to its Google Scholar record; “Read more” opens the project's detailed page.

## Replace the CV and résumé

Export your documents as PDFs and replace `files/cv.pdf` and `files/resume.pdf`, keeping those exact filenames. The viewer, switch, and download links update automatically. Remove the placeholder notice from `_pages/cv.md` once both final documents are ready.

You can write the documents in LaTeX or Overleaf and upload the exported PDFs. The website does not depend on an Overleaf account or an editor-sharing link. The previous text CV is retained in `sources/previous-cv.md` for reference.

## Local preview (optional)

With Ruby and Bundler installed, run:

```text
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Open `http://localhost:4000`. To audit a completed build, run `python tools/check_links.py _site`. Add `--external` to check outgoing links too. `sources/`, `tools/`, and this README are excluded from the published website.
