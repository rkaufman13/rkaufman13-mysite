---
layout: post
title: Customizing the Command Line for Lazy People
categories: things-i-learned
tags: command-line linux
excerpt_separator: <!--more-->
description: The shell is personal. Why not make it customized to your every whim?
---

The shell is personal. Why not make it customized to your every whim?

Actually, there are decent reasons not to go crazy customizing things -- mainly, the logic goes, if you get too invested in having things a certain way that are 'not normal', then when you have to ssh into a remote computer, or god forbid, use someone else's computer, you get hung up. I get it, but also: 95% of the time I'm using my own computer. I want it to be the way I want it.

Things that I have customized that may be of interest:

- colors
- the default prompt
- the default shell (I love fish, but it isn't for everyone)
- the default text editor

#### Colors

You can go pretty crazy with this. Most terminals let you specify the colors in preferences. I don't usually mess around with this but you can. What I do like, however, is setting colors for `ls` - it helps differentiate between types of files. You can set these manually (cheatsheet [here](https://www.zintis.net/LSCOLORS.html)) or use a tool like [lscolors](https://github.com/mzawodnik/lscolors), which works on Mac and Linux. I recommend the latter.

#### The default prompt

At the very least you probably want to show your current git branch, which you can do with this arcane command in your config file:

`export PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ `

Or, I have recently learned, https://bash-prompt-generator.org/ will let you customize to your heart's content. Probably not everything in here will work for every shell but there doesn't appear to be anything too crazy in here, it should work for at least bash and zsh.

#### The default shell

Macs come pre-installed these days with `zsh`, and many people recommend [Ohmyzsh](https://ohmyz.sh/) to make it work the way it "should". Windows machines have Powershell. Linux users...get whatever they get? (I have bash, which is just fine with me). 

This is an unpopular opinion, but having now been using [`fish`](https://fishshell.com/) on my work machine for the past six months, it really is everything a terminal should be.[^1] The way it shares history across all open windows, the intelligent tab completion, and the way it handles multiline commands are *chefs kiss. If you have never tried a shell other than the one that came bundled with your machine, give a couple others a shot!

#### The default text editor

Look, I will only use vim if forced. ([Once you try it, you can't quit--literally!](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/)) If you're better than me, great, keep using vim. But as [this Stackexchange post](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/) points out, "I think there are two reasons it's easy to forget how to exit Vim: developers are often dropped into Vim from a git command or another situation where they didn't expect to be, and they run into it infrequently enough to forget how they solved it last time." If you are tired of being "dropped into Vim" you can make it never happen again with:

`export EDITOR=nano`

in your config file.

Look, I fully admit nano is not a fully featured editor, but when 90% of what I use it for is editing git commit messages and the other 10% is for editing config files, it does the trick, and I never have to remember `:wq`.

[^1]: except POSIX compliant, which will be a deal-breaker for many. I get it. It's a sacrifice I'm willing to make.
