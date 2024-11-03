---
layout: default
title: "python posts"
---
<h2>python</h2>
<ul>
  {% for post in site.tags.python %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
