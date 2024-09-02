---
layout: default
title: "math posts"
---
<h2>math</h2>
<ul>
  {% for post in site.tags.math %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
