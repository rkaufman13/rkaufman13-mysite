---
layout: post
title: "30 Days of coreutils: ls"
categories: things-i-learned
tags: coreutils bash cli
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: ls seems simple, but has a lot going on.
---
{% include coreutils-header.html util="ls" %}

`ls` is how you list files in a directory. Along with many of the other utils I've already covered, this one is also very basic. If you've used the command line, you've used `ls`.

But oh, the options.

`ls`'s default behavior is not so great. It just prints one big line (that can wrap) of all the files in the path you `ls`ed.

```bash
$ ls
file1.txt  file2.txt  file3
```

`ls -l` instead shows your files in a columnar layout with things like permissions, size, the last modified date, etc. This is such a common use case that many people have aliased `ll` to `ls -l`. This is so common, it is even built in to the default `.zshrc` dotfile on the Linux distro I use.

`ls -la` does the same thing as `ls -l` but shows "all" files, including hidden ones. (Files prefixed by a period are 'hidden.') `la` is the common alias.

```bash
$ touch .hidden
$ ls
file1.txt  file2.txt  file3
$ ls -la
.rw-r--r--  0 rkaufman 13 May 10:15 .hidden
.rw-r--r-- 22 rkaufman  6 May 10:20 file1.txt
.rw-r--r-- 20 rkaufman  5 May 13:01 file2.txt
.rw-r--r-- 22 rkaufman  6 May 10:20 file3
```

`ls -1` (that's a numeral 1) gives you the columnar layout without the extra "long" data.

`-t` prints the output sorted in order from most recently created to least. `-s` sorts by size, also descending. `-r` reverses the sort in both cases. (The `-r` flag by itself reverses the default, alphabetical sort, as you'd expect.)

So one could write `ls -lasr` to get all files, sorted by smallest to largest, or `ls -1t` to see a list of files from newest to oldest.

Another great option is `-h` which prints "human-readable" sizes when showing the long file info. By default, `ls`'s size column shows the size of a file in bytes, but `-h` will show file sizes in kb, mb, etc.

The most important option for `ls` is the colors you use to display output, of course, which is set with the LSCOLORS variable, which I briefly wrote about [here]({{site_baseurl | relative_url}}{% link _posts/2025-03-09-customizing-the-command-line.md %}).

And now a confession. I haven't actually used `ls` in years except to write this post; at the recommendation of a coworker a while back, I replaced `ls` with [`eza`](https://github.com/eza-community/eza). It's allegedly faster (I've never noticed), more customizable (yes), and more user-friendly (yes). It's basically a drop-in replacement, and I recommend it highly.
