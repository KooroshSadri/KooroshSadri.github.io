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

{% assign research_items = site.research | sort: 'year' | reverse %}
<div class="research-list">
{% for item in research_items %}
  <article class="research-item">
    <p class="research-meta">{% if item.start_year and item.start_year != item.year %}{{ item.start_year }} &ndash; {% endif %}{{ item.year }}</p>
    <h2 class="archive__item-title"><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a></h2>
    {% include research-authors.html item=item %}
    {% include research-publications.html item=item %}
    <p>{{ item.summary | escape }}</p>
    <p class="research-links"><a href="{{ item.url | relative_url }}">Read more<span class="sr-only"> about {{ item.title | escape }}</span></a></p>
  </article>
{% endfor %}
</div>
