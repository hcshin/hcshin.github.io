---
layout: default
title: "web posts"
---
<h2>web</h2>
<ul>
  {% for post in site.tags.web %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
