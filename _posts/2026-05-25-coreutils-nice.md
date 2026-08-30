---
layout: post
title: "30 Days of Coreutils: nice"
categories: things-i-learned
tags: coreutils cli bash
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: Mom always said to be nice. Here's how to do it in Linux.
---

{% include coreutils-header.html util="nice" %}

For the nice long weekend, I wanted to write about `nice`, which is a command I like purely for its name.

`nice` allows you to modify how "greedy" a process is. The nicer it is, the less CPU priority it gets. A process can be anywhere from -20 (the least nice, the most rude, would cut your grandma off on her way to church) to 19 (the nicest doormat you've ever seen).

Software engineer Robert Elder [gives an excellent example](https://blog.robertelder.org/intro-to-nice-command/):

```bash
$ factor 48324798327489321749327483254325354313 #takes a long time to run
48324798327489321749327483254325354313: 3 3 11 23 3618065157073333 5865845715918448993
$ nice -n 19 factor 48324798327489321749327483254325354313 #takes even longer to run, but doesn't slow down other processes as much
48324798327489321749327483254325354313: 3 3 11 23 3618065157073333 5865845715918448993
$ nice -n -20 factor 48324798327489321749327483254325354313 #runs way faster
48324798327489321749327483254325354313: 3 3 11 23 3618065157073333 5865845715918448993
```

This is a trivial example, of course, but if you have a long-running process that you either want to finish quickly, or that you want to not destroy the rest of your computer, that's what `nice` is for.

`nice` without the `-n` flag automatically makes your process 10 units of niceness nicer. (Units of niceness are a strange concept, but computers can do anything.) To change the niceness of a process that's already running, you can use `renice`. `renice` takes the process ID of the running process as an arg:

`$ renice -n 10 317706`

Interestingly, anyone can make a process nicer, but making one meaner, even back to a baseline level of niceness, is reserved for superusers.

```bash
$ renice -n 10 318494
318494 (process ID) old priority 0, new priority 10
$ renice -n -5 318494 # this would make this process be 5 nice
renice: failed to set priority for 318494 (process ID): Permission denied
$ sudo !!
sudo renice -n -5 318494
318494 (process ID) old priority 10, new priority 5
```

You can see (and set) niceness levels with `htop` and probably other process monitors. And now you know how important it is to be nice.

![Writing this post made me think "Very nice" to myself multiple times, so here's a gif of Sacha Baron Cohen as Borat saying "Very nice!"](/assets/borat-borat-very-nice.gif)
