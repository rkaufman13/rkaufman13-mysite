---
layout: post
title: "Leveling Up on the Command Line, Part 2"
categories: things-i-learned
excerpt_separator: <!--more-->
---

Back on the command line train, chapter 4 of my book is about navigating the filesystem. (To get here, I had to navigate a rabbithole about bash completion, which you can read [here](2024-09-02-complete-rabbithole.md))

- `cd` by itself goes to your home directory
How did I not know this one?



There's a nice section about creating aliases to frequently-used directories, which I've honestly never considered because tab completion+my fast typing means it's not that difficult to switch to `~/my/faraway/directory/with/lots/of/subfolders`. There's sample source code (also [here](https://resources.oreilly.com/examples/0636920601098/-/blob/master/ch04/qcd?ref_type=heads)) to define a `qcd` function that takes tab completion and swaps to any predefined directory. I'm not _massively_ excited about this but may implement it on my work computer anyway.

But here's a trick I've never considered:
`alias bpedit='$EDITOR $HOME/.bash_profile'`
This alias makes it possible to edit your .bash_profile file (I'm still using bash, not `zsh`, don't @ me) from anywhere. Is it that much faster than `nano ~/.bash_profile`? No. Do I think it's cool anyway? Yes.

