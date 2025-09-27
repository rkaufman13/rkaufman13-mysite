---
layout: post
title: Who's Touching My Files? Watch Out With Watchman
categories: things-i-learned
excerpt_separator: <!--more-->
description: A handly tool for just about any use.
image: /assets/game-and-watch.jpg
---

![A photo showing an old (possibly illegitimate as I got it off a .ru site) Game and Watch console.](/assets/game-and-watch.jpg)
*Is Mr. Game and Watch a watch-man? I don't see why not.*

I have a weird setup at work with a lot of interlocking config files. (We sort of halfway support git's [`sparse-checkout` feature](https://git-scm.com/docs/git-sparse-checkout) but with an internal tool that's supposed to keep everything in sync outside of git. Don't ask. It's better than I'm making it sound.)

Anyway because of this funky setup, I was running into an issue where a file was being modified, incorrectly, when I ran _some_ command. I wasn't sure which command was causing the ghost line to reappear, because it kept happening behind my back. It was driving me crazy, and I tried all sorts of solutions to 'catch' the file appearing.

What finally worked was `watchman`, a little file monitor tool that Facebook developed for web development. What it's supposed to do is monitor a directory for changes, and then run some sort of command on changed files. It runs in the background and automatically remembers your watches even if you reboot your machine, which cannot be said for `inotifywait` or `fswatch` or any of the other things I tried. It also works on Windows, Mac and Linux, because under the hood it hooks into one of the above utils depending on your OS. In other words, it Just Works(tm).

The canonical watchman example is running a CSS minifier any time CSS within a certain directory is modified.

`watchman watch path-to-dir`

`watchman -- trigger path-to-dir name-of-trigger '*.css' -- minify-css`

In my case, I don't need to run any sort of processor on changed files, I just need to know *who or what is changing them*.
Easy:

`watchman watch path-to-dir`

`watchman -- trigger path-to-dir mytrigger 'the-file.txt' -- say "I changed"`

This was so silly (and for a while my computer was making a horrendous number of annoying noises) but it worked great and helped me track down which unrelated command was changing my config file.

Learn more about watchman from the [official docs](https://facebook.github.io/watchman/) and give it a shot.

P.S. the official docs have about 3 suggestions for where to find watchman's logs-- I found mine in none of those suggestions, but I was able to run `watchman get-log` to find the (quite mysterious) location.
