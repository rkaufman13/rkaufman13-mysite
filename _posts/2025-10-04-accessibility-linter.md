---
layout: post
title: "Accessibility the Easy Way With Deque's Linter"
categories: things-i-learned housekeeping
tags: accessibility
excerpt_separator: <!--more-->
description: It's not a silver bullet but it can help.
---

I have been interested in, though never an expert in, web accessibility, for years. I believe common-sense affordances like alt text and keyboard navigability in a website are shining examples of the [curb-cut effect](https://ssir.org/articles/entry/the_curb_cut_effect), so while I am not (currently) disabled[^1], I do at least _try_ to make my websites accessible.

But I didn't know until attending [Abbey Perini](https://abbeyperini.dev/home)'s talk at CodeWord last week that I could automate at least some of this work with an accessibility linter.

_Wait, a what?_

Yeah, my reaction too. But just like Prettier or eslint can enforce code style rules, an accessibility linter can enforce, or at least warn you about, accessibility violations. I immediately downloaded deque's [axe Accessibility Linter](https://www.deque.com/axe/devtools/linter/) plugin for VSCode and it's already caught a few things on this here blog. (I may have forgotten alt text in a few places...)

Accessibility is much more than automated tools. A site could pass the linter and pass all kinds of other tests and still be difficult to use. But this is one new tool in my toolbox that I didn't know about before, and I'm glad to have it.

[Watch Abbey's talk for yourself](https://www.youtube.com/live/C9IkpI47UVs?si=5JHpQ4d9JuTJpzxC&t=10314) on Youtube.

[^1]: The stats vary, but some say that 1 in 3 Americans will experience a temporary disability of 90 days or more before reaching the age of 65. That's a lot.