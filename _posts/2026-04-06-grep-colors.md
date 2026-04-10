---
layout: post
title: "Do other people not like colors? or: adventures with ANSI codes and grep"
categories: things-i-learned
tags: bash
excerpt_separator: <!--more-->
description: It only ever seems to happen to me.
---

![A screenshot of someone's terminal (not mine) showing a very hackerman-ish ASCII art logo in bright green and red.](/assets/hackerman.png)
*The better your terminal colors are, the better a coder you are. That's just science.*

I have `GREP_OPTIONS=--color=always` set, because I like to be able to see what I found.

This can cause issues, however, because the color option outputs literal characters to the output stream.

If you search for "error" in a file:

`$ grep --color=always "error" file.txt`

The actual output sent to the terminal is:

`This is an \033[01;31merror\033[0m message`

The terminal then interprets this to mean:

<code>This is an <span style="font-weight:bold;color:red">error</span> message</code>

This is very cool, colors are useful. Helps me find the exact thing I searched for.

But let's say your company has two build scripts that are chained together, for some reason. The first one generates a value and writes it to a file as `export VAR=abc123`. The second one includes this line:
`local_var_to_do_something_cool_with=$(grep -m1 "^export VAR=" ~/.zshrc 2>/dev/null | sed "s/^export VAR='\(.*\)'$/\1/")`

In other words, find the first (`-m1`) instance of a line starting with `export VAR=` in the `~/.zshrc` file, and then use `sed` and regex to retrieve everything in the first capturing group that matches the pattern, and reads the value back into a local variable. (I'm not going to try to explain regex today, trust me it works. Also, no, writing a variable to a file and then reading it back in a separate script isn't efficient...don't ask.)

Can you see where this is going? The results of the first grep, with `--color=always`, returns a string that looks like this:
`\033[01;31mexport VAR=\033[0mabc123`.

Which doesn't match the string `sed` is looking for when the output is piped in.

The folks working on this set of scripts didn't notice, because they don't use color when grepping. I came along as a user of the script and spent multiple days whining that "it didn't work," until I had a few minutes to dig into the code today.

The easy fix is to put `unset GREP_OPTIONS` at the top of the script.

TBH it should be required, just like [`set -euo pipefail`](https://gist.github.com/mohanpedala/1e2ff5661761d3abd0385e8223e16425).

In the course of writing this post, however, [I learned that](https://www.gnu.org/software/grep/manual/grep.html) "The GREP_OPTIONS environment variable of grep 2.20 and earlier is no longer supported, as it caused problems when writing portable scripts." No kidding.

Again, from the manual:

"For example, if grep is in the directory ‘/usr/bin’ you can prepend $HOME/bin to your PATH and create an executable script $HOME/bin/grep containing the following:"

```bash
#! /bin/sh
export PATH=/usr/bin
exec grep --color=auto --devices=skip "$@"
```

So I'm apparently not the only one to get tripped up by this, but I'll be setting up the suggested fix tomorrow...

#### Additional reading

- [Julia Evans on terminal colors](https://jvns.ca/blog/2024/10/01/terminal-colours/)