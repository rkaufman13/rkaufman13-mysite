---
layout: post
title: Building a Cookbook in Python, for Reasons (Part 2)
categories: stuff-i-made
excerpt_separator: <!--more-->
project: "The Brookland Dish"
description: Jekyll-izing and making a github PR via API.
---

In my [last post]({{site.baseurl}}{%link _posts/2025-12-12-recipe-buddy-part1.md%}), I talked about building a cookbook/recipe blog that stores recipes emailed to a special address. I talked about setting up the backend, the service that provides an 'email received' webhook, and the library that parses recipe information from a website using the Schema.org standardized schema.

Where we left off, we had just grabbed all the information about a recipe -- name, ingredients, cook time, etc., and dumped them into a Python dict. Now, we can inject them into a Markdown template for use by Jekyll.

Loyal readers of this blog know that I'm a huge Jekyll fan. It's so easy to create new static HTML files from a basic template.

In my case, the template looks something like this:

```markdown
---
layout: post
title:  {%raw%}{{title}}
source_site: {{source_site}}
source: {{canonical_url}}
....and so on
---

### Ingredients
{{ingredients}}

### Instructions
{{instructions}}{%endraw%}
```

Everything between the `---` lines is considered "front matter" and can be used as data to be injected into a post, or metadata about a post, etc.

Our `templatizer` just needs to read in this file and call a bunch of `replace()`s. It looks something like this:

```python
{%raw%}
    RECIPE_TITLE = "{{title}}"
    RECIPE_SOURCE = "{{source_site}}"
    RECIPE_URL = "{{canonical_url}}"{%endraw%}
    with (open(TEMPLATE_FILE, 'r') as template):
        buffer = template.read()
        buffer = buffer.replace(RECIPE_TITLE, recipe.get("title"))
        .replace(RECIPE_SOURCE,recipe.get("site_name"))
        .replace(RECIPE_URL,recipe.get("canonical_url"))
        #and so on
```

The templatizer also generates a file name based on the slug of the recipe and the date it was shared (not the date it was initially posted on the source site). Anyway, this is all relatively simple.

But now we have to... *dun dun dunnnnnn* talk to Github.

### Talking to Github

I wanted a human in the loop here. This is not a high-traffic application and my endpoint is semi-insecure, so if someone were to start spamming it with junk data...there's not much they could accomplish, but there's *less* they can accomplish if I have to manually approve every recipe first. So while it's fairly easy to force-push directly to main with the Github API, I wanted my app to create a PR instead.

It could be worse, Github's documentation is pretty good, and they make it real easy to make a scoped personal access token just for the actions you need to take. I won't walk you through every step of code that needs to happen here, but the general steps are:

```python
def do_github_stuff(content, filename): #i'm good at naming things
    main_sha = get_branch_sha("main") # gets the hash of the tip of main
    new_branch, new_ref, branch_name = create_new_branch(main_sha) #creates a new branch off of main, basically the same as doing git checkout -b newbranch. I'm generating the branch name inside this function but if it's easier to understand, just imagine that instead of returning the branch name, I'm passing in "newbranch"
    new_sha = create_tree(new_branch.get('object').get('sha'), content, filename) #adds my new file to the new branch
    new_commit = create_commit(new_sha, main_sha) #creates the commit; unlike doing a commit via command line,  we explicitly have to tell git who the parents and children of the commit are. this returns a new hash
    update_ref_pointer(new_ref, new_commit) #now we have the new ref (/heads/mybranch/) and the new hash of the commit, this forces the tip of the new branch to point to the newly created hash
    create_pull_request(branch_name, filename) #the second argument here is actually the name of the PR, which in this case is just generated as f"adds {filename}"
```

That feels like a lot, and in some ways it is, but in other ways it's just five POSTs.

All I can say is thank goodness I watched that [presentation about git commit hashes]({{site.baseurl}}{% link _posts/2025-04-28-git-commit-hash.md %}) earlier this year or this would have been significantly more difficult.

### The frontend

I did the basic Github Pages/Jekyll setup. In doing so, either I missed a step, or the setup is missing some steps. When I clicked the setup button, I got:

- a repo with a deploy github action that installed the wrong version of Ruby
- nothing else? So then I did `jekyll new` on my local machine to spin up a new site, but the default settings in `config.yml` weren't appropriate for a site hosted on Github Pages. It turns out that Github [does have docs on how to configure ](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll) Jekyll, but I wish the button did more of this for me.

Anyway! Did manage to get up and running, finally. However, only a *handful* of the Github Pages-supported Jekyll themes are set up for blogs. (Minimal, minima, and hacker, for those keeping score). If you want to use a different theme, you'll have to override some theme defaults. Which is fine, there's excellent documentation [on Jekyll's site](https://jekyllrb.com/docs/themes/#overriding-theme-defaults) about doing so.

So now this thing is hooked up! We just have to subscribe our email robot to our listserv and wait for the recipes to come rolling in.

![A Spongebob-style title card reading "Three days later..."](/assets/three_days_later.png)

Nobody has posted a recipe! This is a disaster! No, actually it's just a pretty low-traffic, and it shouldn't be surprising that three days in we have nothing. But I'd like to seed the site with some examples so it's not just empty.

This listserv has been hosted on Google Groups for the last few years (we are currently in the process of de-Googling due to [unrelated issues](https://support.google.com/a/thread/203495386/why-are-my-emails-to-a-group-being-sent-to-moderation?hl=en)), and say what you will about Google, they at least do let you export your data. As a moderator of the listserv, I have access to the entire group's message history. So I made a [Google Takeout](https://takeout.google.com/?pli=1) request.

![A Spongebob-style title card reading "Three days later..."](/assets/three_days_later.png)

A few days later, a zip file containing my data was sent to me. All the messages are there...as one giant `.mbox` file. 

Luckily, this is a solved problem. Using [this gist](https://gist.github.com/benwattsjones/060ad83efd2b3afc8b229d41f9b246c4) as a reference, I was able to parse every email and look for ones that contained URLs. Pulled about 10 random ones out and fed them to my API, which was able to successfully parse half of them, anyway that's how I ended up becoming a contributor to the recipe-parser library.

In all seriousness this was a very rewarding project. I love when something comes together in a weekend or two (it's taken me longer to write up this series of posts than to actually create the project), and I love when tech can be used to make something not that scales to a billion people, but solves a specific problem for ten people. Or maybe just even me, I'm not sure the rest of my potluck group cares. :) But I got to learn about FastAPI, email webhooks, and get more familiar with Jekyll. I count that as a big, delicious win.
