---
title: "A title for your post"
excerpt: "A short summary for the homepage."
layout: single
author_profile: true
comments: false
share: false
related: false
---

This is an unpublished example. Replace this text with your post, then move the file to `_posts/YYYY-MM-DD-your-title.md` with the publication date in its filename.

Use ordinary Markdown for paragraphs, headings, lists, and links. Math can be written as `$E = mc^2$` inline or between `$$` on separate lines.

For a YouTube video, put this include between paragraphs, replacing the video ID and title:

{% raw %}
```liquid
{% include youtube.html id="VIDEO_ID" title="A descriptive video title" %}
```
{% endraw %}

Videos will resize with the page.

Drafts are not published by the normal site build.
