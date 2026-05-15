---
layout: post
title: "30 Days of coreutils: cat"
categories: things-i-learned
tags: coreutils bash cli
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: Nothing to do with pets, unfortunately.
---

{% include coreutils-header.html util="cat" %}

`cat`, short for concatenate, prints the output of a file or files to the console.

```bash
$ cat file.txt
Hello, I am a file
```

I almost always use it with one file, but it's also possible to combine two files into one output, which, given the name of the util, is probably what it was originally designed for:

```bash
$ cat file.txt file2.txt
Hello, I am a file
Hi, I am also a file
```

`cat` has some very useful flags, most of which are new to me.

`-n` prints each line of the file prefixed with a line number. (`-b` only adds line numbers to non-blank lines; as always, these Linux guys had a great sense of humor when coming up with these flags.)

`-A` shows non-printing characters (such as tabs and line-breaks).

`-s` removes consecutive blank lines, collapsing them into a single line.

```bash
$ cat badly_formatted_file.txt
This is just to say



I have eaten


The plums

$ cat -s badly_formatted_file.txt
This is just to say

I have eaten

The plums
```

`cat`'s cousin `tac`, which is part of GNU coreutils but not part of the BSD version of them (:shakes fist: darn you, Steve Jobs!) does exactly what `cat` does, but reverses the order of lines. It's not that useful, honestly, but it is a fun party trick, for certain definitions of "party."

```bash
$ tac file2.txt file1.txt 
Hi, I am also a file
Hello, I am a file
```
