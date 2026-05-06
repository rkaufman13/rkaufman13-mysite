---
layout: post
title: "30 Days of coreutils: mkdir"
categories: things-i-learned
tags: coreutils bash cli
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: mkdir
---

{% include coreutils-header.html util="mkdir" %}

A very common command - `mkdir` creates a new directory.

If you try to create nested directories, you'll get an error if any of the intermediate directories don't exist:

```bash
$ mkdir foo/bar/baz
mkdir: foo/bar: No such file or directory
```

The `-p` flag, which according to the man page stands for "parents" (I need to know the meanings of these flags or I'll never remember them) will create the intermediate directories for you.

```bash
$ mkdir -p foo/bar/baz
$ ls foo/bar
baz
```

You can also create multiple directories in one command:

```bash
$ mkdir foo bar baz
$ ls
foo bar baz
```

Fun fact, a system with only `find` and `mkdir` is (allegedly) Turing complete. At least, [this website](https://ogiekako.vercel.app/blog/find_mkdir_tc) claims it is, and the proof seems legit.
