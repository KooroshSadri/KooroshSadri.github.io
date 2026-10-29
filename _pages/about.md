---
layout: archive
permalink: /
title: "About"
excerpt: "Koorosh Sadri — theoretical physics, research, and notes."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class = "home-intro" markdown = "1">
I’m Koorosh Sadri, a physics Ph.D. student at Pennsylvania State University. I work in theoretical physics, with interests in photonics, nonlinear dynamics, nonlinear photonics, and quantum information as well as classical gravitational physics. Broadly speaking, I’m drawn to finding clear mathematical descriptions of physical phenomena.
</div>

{% assign blog_posts = site.posts | sort: 'date' | reverse %}
{% if blog_posts.size > 0 %}
<section class="blog-post-list" aria-labelledby="posts-heading">
  <h2 id="posts-heading">Posts</h2>
  {% for post in blog_posts %}
  <article class="archive__item blog-post">
    <h3 class="archive__item-title"><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
    <p class="page__meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%B %-d, %Y' }}</time></p>
    {% if post.excerpt %}<div class="archive__item-excerpt">{{ post.excerpt | markdownify }}</div>{% endif %}
  </article>
  {% endfor %}
</section>
{% endif %}
