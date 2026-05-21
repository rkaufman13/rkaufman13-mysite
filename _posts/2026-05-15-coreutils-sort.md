---
layout: post
title: "30 Days of coreutils: sort"
categories: things-i-learned
tags: coreutils bash cli
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: A program that has been superseded by modern GUI-based tools, but still has plenty of uses.
---

{% include coreutils-header.html util="sort" %}

We're getting into some of the more weeds-y commands here; not because these aren't useful, but because in the world of GUIs, I feel there's less need to sort output on a command line. (I might, for example, upload a CSV to google sheets and sort it there, or use Python.) But if I did have a need to sort something in the command-line only, that's what sort is for.

`sort` can take input from one or more files and sorts them line by line. If more than one file is provided, the output is merged.

```bash
$ cat file1.txt
This file\'s contents start with the letter "T"
$ cat file2.txt
A file that starts with the letter "A" should come first
$ sort file1.txt file2.txt
A file that starts with the letter "A" should come first
This file\'s contents start with the letter "T"
$ cat longfile.txt
Giraffe
Baboon
Monkey
Armadillo
Zebra
$ sort longfile.txt
Armadillo
Baboon
Giraffe
Monkey
Zebra
```

`sort` can also read from standard input, of course:

```bash
$ du /bin/* | sort -n
4       /bin/domainname
24      /bin/ls
102     /bin/sh
304     /bin/csh
```

I think where it gets really powerful is on columnar data (like the kind of thing I would upload to google sheets). You use the `-k` option for that. Here's an example from [Wikipedia](https://en.wikipedia.org/wiki/Sort_(Unix)):

```bash
$ cat zipcode
Adam  12345
Bob   34567
Joe   56789
Sam   45678
Wendy 23456

$ sort -k 2n zipcode
Adam  12345
Wendy 23456
Bob   34567
Sam   45678
Joe   56789
```

Finally, [here's](https://unix.stackexchange.com/questions/11856/sort-but-keep-header-line-at-the-top/11859#11859) a rather lovely little snippet that keeps the top line of the input as the top line, so that a sorted file (or any input) with a header keeps the header at the top. I'm adding this to my dotfile right now.
