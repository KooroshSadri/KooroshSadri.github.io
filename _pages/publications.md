---
layout: archive
title: "Research"
excerpt: "Research in photonics and quantum information, with paper links and short explanations."
permalink: /research/
author_profile: true
redirect_from:
  - /publications/
  - /publications.html
---

Research projects and papers, with a short explanation of the questions and results.

{% assign research_items = site.research | sort: 'year' | reverse %}
<div class="research-list">
{% for item in research_items %}
  <article class="research-item">
    <p class="research-meta">{{ item.year }} · {{ item.status | escape }}</p>
    <h2 class="archive__item-title"><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a></h2>
    <div class="research-authors">{{ item.authors | markdownify }}</div>
    <p class="research-venue">{{ item.publication | escape }}</p>
    <p>{{ item.summary | escape }}</p>
    <p class="research-links"><a href="{{ item.url | relative_url }}">Read more<span class="sr-only"> about {{ item.title | escape }}</span></a>{% for link in item.paper_links %} <span aria-hidden="true">·</span> <a href="{{ link.url | escape }}">{{ link.label | escape }}<span class="sr-only">: {{ item.title | escape }}</span></a>{% endfor %}</p>
  </article>
{% endfor %}
</div>
