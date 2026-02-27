---
layout: post
title: "Why I Switched to git switch"
categories: things-i-learned
excerpt_separator: <!--more-->
description: Why understanding the commit hash helps understand why git goes wrong.
---
![Git is too hard.](/assets/git-is-too-hard.png)

When I first learned[^1] git, I learned that to stop working in the current branch and to start working in a new branch, the command was `git checkout branchname`. Or to create a new branch, `git checkout -b branchname`.

All the way back in 2019, though, the git team released `git switch`, which is supposed to replace `git checkout`. (Don't worry, `checkout` [isn't going anywhere](https://github.com/git/git/blob/028bb23a61653dde0481671a2ac4a4e83ce061b8/Documentation/BreakingChanges.txt#L124-L135).) And finally, this year, I retrained my muscle memory to use `git switch` instead of `checkout`. Why is switch better?

1. `checkout` tries to do too many things. `git checkout <branchname>` is valid, as is `git checkout <hash>`, as is `git checkout -- path/to/file`. These all do different things. Checking out a **branch* means "start working on this branch." Checking out a *commit hash* puts you in "detached HEAD" state, the source of many a developer's footgun.[^2] Checking out a *file* reverts it to a previous state (usually to the state of the last commit).

     I've used all these use cases! Usually on purpose! But you have to admit it's kinda confusing.

     Also, if you have a file and a branch that have the same name, git has to decide which one you meant when you use `checkout`. I've never come across this particular collision myself but I can imagine there are a non-zero number of git branches called `readme` out there, which could lead to really unexpected results if you just typed `git checkout readme` without looking closely at the output.

2. The way to create a new branch with `switch` is to use the `-c` flag, which means "create." The way to create a new branch with `checkout` is to use the `-b` flag, which means "branch," which is a tautology.

Basically, as I understand it, the git team felt that `checkout` did too many things and was confusing for new users. All good reasons to split the command into two.

Most important to me, however, is `git switch -` which switches back to the previous branch, similar to other Unix-y commands, such as `cd -` , which takes you back to your previous directory.

As always, saving like two keystrokes is the only thing I care about. Efficiency!

[^1]: Nobody has learned git. We all just type random things into our terminal until it works or we have to do a `git push --force`.
[^2]: I still don't fully understand what a `detached HEAD` is.
