---
layout: post
title: "The Surprising Power of Jekyll's site.data"
categories: things-i-learned
excerpt_separator: <!--more-->
description: How and why to turn Jekyll into a database
tags: jekyll
image: /assets/database.jpg
---
![A stereotypical, "hacker-like" depiction of a database, with glowing blue lines signifying connections between tables.](/assets/database.jpg)

I've been speaking a lot this past year. This is new and exciting to me, and I want to track all my accomplishments, because each one of them feels new, exciting, and honestly a little scary. So keeping track of everything is a great way for me to mark these accomplishments (I may also have had a [donut](https://larahogan.me/donuts/) after my last talk at Momentum).

But do I want to manually update [this page]({%link speaking.md%}) every time something changes? Heck naw. This is structured data, and Jekyll should treat it as such.

## Enter site.data

Enter `site.data`. Any structured file (JSON, YAML, CSV or TSV) you place in your Jekyll `_data` folder will become accessible as `site.data.filename` [^1]. You can then access it like any other variable. Jekyll is smart enough to interpret your file as a list which you can sort, filter, etc.

What this means is I can create a CSV like this:

```csv
event_date,venue,talk,link
2025-10-16,Momentum Dev Con,Get Unblocked Faster,,
....
```

 and then access it via:

```html
{%raw%}
{% assign all_appearances = site.data.speaking_appearances | sort:'event_date' %}

<h2>Upcoming</h2>
{% for row in all_appearances %}
{% assign date_to_check = row.event_date | date: '%s' %}
{% if date_to_check > current_date %}
<p> {{row.event_date | date: '%B %d, %Y'}}:
{%if row.link%}
<a href="{{row.link}}">
{%endif%}
{{row.talk}} -
{%if row.link%}
</a>
{%endif%}
{{row.venue}}
</p>
{%endif%}
{% endfor %}
{%endraw%}
```

This looks like a lot if you're not used to Liquid syntax, but it's basically a fancy templating language. On the first line, we assign a variable to hold the "list of stuff in site.data.appearances, sorted by event_date" (which is one of the headers in the CSV). Then we loop through each item in the list and compare its date, which has been converted to a UNIX timestamp, to the current date (which I assigned earlier in the template). If the item has a date in the future, we render it to the page, optionally with a link to the source material.

This is already a huge time-saver, and means that all my dates, links, etc., will be rendered consistently, and I can change their styling/look without having to manually copy and paste.

But let's not stop there. I don't want to manually update a CSV that lives on my home computer (or in a github repo), that sounds boring. So inspired by my husband [Chris Combs](https://chriscombs.net) who has set up something similar, let's automate this!

## Enter a database that is not a database

Google Sheets is not a database, although I wouldn't be the first person to use it as such. And for a simple way to store (a small amount of) structured data[^2], it's pretty darn good.

So I copy my CSV from above into a google sheet and publish it to the web as a CSV. This does make the CSV publicly accessible for anyone who knows the URL, but I'm not storing any PII in here, so it's fine. Then, as an extra line in my [custom deploy pipeline](https://www.readwriterachel.com/things-i-learned/2025/07/12/rakefiles.html) as well as my custom preview script, I add:

```bash
wget https://docs.google.com/spreadsheets/link/to/spreadsheet?output=csv --output-document=${SITE_ROOT_DIR}/_data/speaking_appearances.csv || echo "Something went wrong"
```

This means that every time I deploy, or launch a local version of the site with `bundle exec jekyll serve`, I get the most up-to-date version of the Google sheet, which I can update from anywhere.

Jekyll is still a static site generator, so I still have to deploy to see the most recent changes, but that works for me, for this thing that is only semi-regularly updated anyway. If this is not for you, you probably already know that and will not use Jekyll.

I hope this was useful! I definitely think there's a lot more that can be done with Jekyll's datafiles and I can't wait to come up with more insane ideas.

### Further reading

- Jekyll's official site has some [very cool examples](https://jekyllrb.com/docs/datafiles/) of things you can do with a datafile.

#### Footnotes

[^1]: for this reason you should avoid having two files with the same base name but different extensions. Which seems like a silly limitation but oh well.

[^2]: if I give ten million talks this solution may not scale. But I think a number of things about this hypothetical would become unsustainable first.
