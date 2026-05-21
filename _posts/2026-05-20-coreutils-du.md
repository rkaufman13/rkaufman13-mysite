---
layout: post
title: "30 Days of Coreutils: du"
categories: things-i-learned
tags: coreutils cli bash
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: What's taking up all that space on your computer and why is it always Docker?
---

{% include coreutils-header.html util="du" %}

`du` is short for `disk usage`, although some people say it is short for `device usage`[^1], and allows you to see the size of files on your system. By default, `du` inspects the size of all subdirectories starting from your working directory.

```bash
$ ls -l
-rw-rw-r-- 1 rachel rachel    20 May 18 13:35 file1.txt
-rw-rw-r-- 1 rachel rachel  9025 May 18 13:39 file2.txt
-rw-rw-r-- 1 rachel rachel 31007 May 18 13:39 file3.txt
$ du -a
12 ./file2.txt
4  ./file1.txt
32 ./file3.txt
52 .
```

(The `-a` flag is necessary to see files in the directory, otherwise `du` only prints the cumulative size of the subdirectories reachable from the working directory. Because just getting the size of files in a single directory is useless, since you can already do it with `ls -l`. But this is a contrived example.)

By default, the output is sorted ...  I'm actually not sure, and the man page doesn't answer that question...But it's not sorted by anything useful, for sure. We can fix this with our friend [`sort`]({{site.baseurl | relative_url}}{% link _posts/2026-05-15-coreutils-sort.md %})!

```bash
$ du -a | sort -nr
52  .
32  ./file3.txt
12  ./file2.txt
4  ./file1.txt
```

These are weirdly round numbers, right? That's also because `du` rounds to the nearest 4KB "block" of size, so our 20-byte file takes up 4 "blocks". We can see this with `du -ah` (just like with [`ls`]({{site.baseurl | relative_url}}{% link _posts/2026-05-13-coreutils-ls.md %}), `-h` prints "human-readable" file sizes):

```bash
$du -ah
12K  ./file2.txt
4.0K ./file1.txt
32K  ./file3.txt
52K  .
```

If we want to sort by human-readable file size, we must also apply the `-h` to sort (which is supported in GNU coreutils only - again Mac users, you're out of luck):

```bash
$ du -ah | sort -hr
52K  .
32K  ./file3.txt
12K  ./file2.txt
4.0K ./file1.txt
```

This becomes more powerful if you're scanning an entire folder and all its subdirectories. With [`sort`]({{site.baseurl | relative_url}}{% link _posts/2026-05-15-coreutils-sort.md %}) and [`head`]({{site.baseurl | relative_url}}{% link _posts/2026-05-18-coreutils-tail.md %}), both of which we've covered already, we could do:

```bash
$ pwd
/var
$ sudo du -ah | sort -hr | head -n 10
32G  .
23G  ./cache/apt
23G  ./cache
22G  ./cache/apt/archives
8.0G ./lib
7.2G ./lib/docker
6.9G ./lib/docker/overlay2
1.3G ./cache/apt/archives/linux-firmware_20250317.git1d4c88ee-0ubuntu1+system76~1763137702~22.04~f3aeef4_amd64.deb
1.3G ./cache/apt/archives/linux-firmware_20250317.git1d4c88ee-0ubuntu1+system76~1749060582~22.04~230e2f0_amd64.deb
1.2G ./log/journal/3edf9a174d8cb6f9266525396674ab40
```

This shows me that in the `/var/` directory, Docker takes up a lot of space, surprise surprise.

One last thing -- we can also limit the depth that `du` traverses with the `-d` flag, for max depth.  `-d2` means that `/cache/apt/archives` won't appear in the final list, nor would `lib/docker/overlay2`.

In other words:

```bash
sudo du -ah -d2 | sort -hr | head -n 10
32G  .
23G  ./cache/apt
23G  ./cache
8.0G ./lib
7.2G ./lib/docker
1.2G ./log/journal
1.2G ./log
472M ./lib/apt
111M ./lib/dpkg
62M  ./lib/postgresql
```

That's a pretty useful way to see the largest directories on your system, without going too deep into the weeds.

What are your use cases for `du`? Let me know.

[^1]: because not every type of storage is a "disk". Unix nerds are fun at parties.

