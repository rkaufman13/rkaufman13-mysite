---
layout: post
title: "Cool Discovery: Over the Wire's Wargames"
categories: things-i-learned
tags: command-line linux
description: How to become a 1337 h4xx0r in 20 easy steps.
excerpt_separator: <!--more-->
---

I was nerd sniped this weekend by a coworker who told me about [Over The Wire's wargames](https://overthewire.org/wargames/), which are self-directed cybersecurity challenges. I am just about halfway through the easiest one, [Bandit](https://overthewire.org/wargames/bandit/), which in addition to having me scan for open ports and base64 decode strings, is also teaching me quite a few new command-line tricks. Here's a little random selection:

- `sshpass` is a fun little utility that lets you enter your ssh password in visible text on the command line. This seems like a terrible idea to use with a production server that you care about, but these games have me storing 30 separate passwords and I want to make sure I'm putting in the right one, and I'm not worried about someone hacking Over the Wire.
- Have a weird binary that you don't know what to do with? `strings` will print any human-readable set of characters that it finds. Useful for playing CTF challenges and probably other things.
- `grep -v thingyoudontwant` will display records that DON'T match the phrase. The `v` stands for in**v**ert, clearly.

Off I go to hack into the next level...
