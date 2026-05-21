---
layout: post
title: "30 Days of coreutils: ln"
categories: things-i-learned
tags: coreutils linux cli
excerpt_separator: <!--more-->
description: Today we dive into hard and soft links.
project: "30 Days of Coreutils"
---

{% include coreutils-header.html util="ln" %}

`ln` means `link` and is used to create "linked files" pointing to source files.

In the words of the man page, "It is useful for maintaining multiple copies of a file in many places at once without using up storage for the “copies”; instead, a link “points” to the original copy."

This is an okay description, I like to think of links as what Macs call "aliases" and Windows calls "shortcuts." Feel free to use that mental model if it helps you, although I don't know if they're exactly the same.

`ln -s` is the most common (I think) usage of the `ln` util, and it creates what's called a "symbolic link" or symlink. Without the `-s` flag you create a "hard link."

I found these distinctions difficult to grok, but I think the main difference is that you can safely delete an original file and retain a hard link, but with a symlink, if you delete the original, symlinks will break because they are now pointing to nothing.

Symlinks show up when you run `ls -l` (coming in a future post) like so:

```bash
shortcut -> file1.txt
```

If I were to then `rm file1.txt` and then `ls -l` again, on my system there's a nice red warning telling me that there's an orphaned symlink:

![A screenshot showing `shortcut -> file1.txt` but in a deep warning red](/assets/ln.png)

There are quite a few other flags available for `ln` which honestly I don't think are that useful in 2026. But basic symlinks are very powerful, and they pop up everywhere in Linux systems (such as the [sites-available/sites-enabled pattern](https://www.reddit.com/r/devops/comments/b7g9wo/comment/ejriqmn/) on both apache and nginx servers[^1].)

#### Further reading 

- [A Youtuber explains how to use `ln` in gaming](https://www.youtube.com/watch?v=mA08E59-zo8)
- [A very detailed explanation of some other uses for `ln`](https://superuser.com/a/384887)

[^1]: At least on Debian-based machines, because of course there are differing opinions on how this should work.
