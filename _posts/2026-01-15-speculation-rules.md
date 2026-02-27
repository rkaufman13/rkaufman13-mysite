---
layout: post
title: Making This Blog Even Faster With Speculation Rules
categories: things-i-learned housekeeping
excerpt_separator: <!--more-->
description: A one-line change that is really not necessary, but is fun.
image: /assets/speed.jpg
---

![A man on a bike going so fast that the background is just a series of blurred lines.](/assets/speed.jpg)

Browsing the [HTMHell Advent Calendar](https://www.htmhell.dev/adventcalendar/2025/3/) I learned about a completely new-to-me browser API called "speculation rules." This poorly-named (according to me) feature allows browsers to prefetch or even pre-render content speculatively, basically predicting what a user is going to click on. Currently, this feature is available in Chromium-based browsers, but Safari and Firefox are working on it, and in the meantime, including it doesn't harm the experience for Firefox and Safari users.

In its most basic form, adding the following to a page:

```html
<script type="speculationrules">{  "prerender": [{    "where": { "href_matches": "/*" },    "eagerness": "moderate"  }]}</script>
```

is all it takes to pre-render the destination link when a user hovers their mouse over it, making the load almost instantaneous from the user's perspective.

The author of the blog post, Barry Pollard, who works on Chrome at Google, [goes on to explain some of the quirks of `speculationrules`](https://www.htmhell.dev/adventcalendar/2025/3/). For example, how do you handle mobile users, where "hover" isn't a thing? What about Javascript that you don't want to execute before the page is actually viewed? (What about analytics where you don't want to count page views before the user actually looks at the page?) These are problems that are "actively being worked on," which means not solved just yet. I would not use this feature on a production site where I cared about any of those things.

This is a progressive enhancement to `<link rel="prefetch">` which is more widely supported. But the old way seems harder to implement as, at least by my read of [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch), I would have to consider exactly what links are most likely to be loaded next by the user on what pages, whereas the speculation rules API decides for me based on the user's actions.

To sum up, this is a pretty neat option that is definitely not yet ready for use on all sites. There are a lot of questions that need to be answered. But in the meantime, I think speculation rules are a perfect fit for a static, no-JS site like this blog. Which is already pretty fast, by dint of it being a static, no-JS site. 🤷

If you're using Chrome and want to check out the new behavior for yourself, simply open Devtools, navigate to the Network tab, then hover over any link on this site. You'll see a little blip of activity before you click. Neat!
