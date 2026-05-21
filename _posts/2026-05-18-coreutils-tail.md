---
layout: post
title: "30 Days of coreutils: head and tail"
categories: things-i-learned
tags: coreutils bash cli
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: Catch a cat by the tail (or head).
---
{% include coreutils-header.html util="tail && head" %}

`tail` and `head` are incredibly useful tools for monitoring processes, ones that I honestly don't use enough. These programs output the first part of files (`head`) or the last (`tail`).

`tail` is very frequently used with the `-f` option which means that the program will continue to output lines as the file grows, basically giving you real-time insight into, for example, new logs being written to a file.

`tail -f /var/log/syslog` will show the last 10 lines of that file, and append new lines as they are added. (As always, hit ctrl-c to exit.)

The `-F` flag is the same as `-f` but will automatically try to reopen the file if it is inaccessible (e.g. if logrotate is rotating your logs). This flag doesn't exist on the Mac version of tail, sadly.

You could also use `tail` to print "summaries" of CSV files, assuming you had something like a 'totals' row at the bottom. Especially combined with the `-n` flag, which changes the number of lines output from the default 10 to whatever you specify.

Given:

```csv
Month, sales,
January, 10,
February, 20,
March, 5,
YTD Total, 35
```

then `tail -n 1 sales.csv` would print:
`YTD Total, 35`

And `head -n 1 sales.csv` would print the columns, if you had a need for that.

```bash
$ head -n 1 sales.csv
Month, sales,
```