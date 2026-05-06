---
layout: post
title: "30 Days of coreutils: cp and mv"
categories: things-i-learned
tags: coreutils bash cli
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: Starting off with a twofer, becaues why not.
---

{% include coreutils-header.html util="cp && mv" %}

Starting us off with two very basic commands: `cp` and its cousin `mv`. `cp` means "copy" and copies a file from one location to another. `mv` means "move" and, you guessed it, moves a file from one location to another. If you have used the command line at all, you've probably used these lil friends.

What secrets do these guys hold, though?

I've recently learned about the `-i` flag, which, according to the man page, means "interactive", which is confusing, but it is a way to prevent yourself from accidentally overwriting files while copying or moving.

A simple example:

```bash
$ touch first
$ touch second
$ mv first second
$ ls
second
```

In this example, `first` was renamed to `second` and overwrote the initial contents of `second`.

But:

```bash
$ touch first
$ touch second
$ mv -i first second
mv: overwrite 'second'?
```

This is great and I immediately aliased my `cp` and `mv` commands to include `-i`.

The counterargument for doing this is that you'll get so used to the safety net of having this that you'll be more likely to make mistakes on other computers. I don't really buy this logic, but people argue passionately about it online.

You can also use `-n` which will mean "don't ask to overwrite a file, just fail if it would", and `-f` which overwrites no matter what. If you have more than one of these flags in your command, the last one "wins."

You could also instead choose to use the `-b` (backup) flag, which allows the move or copy to go through, but keeps a copy of the overwritten file.

```bash
$ touch first
$ touch second
$ cp -b first second
$ ls
second second~
```

I doubt I'll find a ton of use for this but it is definitely something built into both these commands that I'd never heard of before, which is the point of this series!

There's also `-u`, another flag shared by `cp` and `mv`, which stands for `update`, which means "only copy/move when the source file is newer than the destination file, or there is no destination file". (I do think something more modern like `rsync` is a better tool for this kind of thing but good to know the authors of these utils were thinking about this scenario.)

Finally, if you are copying or moving multiple files into a directory (rather than renaming a single file), you can do it in one line!

```bash
$ cp first second third /backup/
$ ls /backup
first second third
```

Extra-finally, this is not technically part of the coreutils implementation of `cp` and `mv`, but apparently enough people have wished that they had progress bars that someone [made one](https://github.com/Xfennec/progress). Presented with curiosity and intrigue, but without endorsement.

**Update**: I wrote this on my personal (Linux) laptop, and then tried to put a few of my own tricks into play on my work laptop, a Macbook. Should be noted that Macs ship with the BSD versions of these utils, which have very slight differences from the GNU coreutils. You can install many of the GNU coreutils on a Mac with homebrew (see [this Stackoverflow answer](https://apple.stackexchange.com/questions/69223/how-to-replace-mac-os-x-utilities-with-gnu-core-utilities); they'll be prefaced with `g` (for GNU) by default.)