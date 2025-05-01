---
layout: post
title: "Secrets of the Git Commit Hash"
categories: things-i-learned
excerpt_separator: <!--more-->
description: Why understanding the commit hash helps understand why git goes wrong.
image: /assets/git-is-too-hard.png
---

![this image simply is of the text: "git is too hard"](/assets/git-is-too-hard.png)

I attended an online presentation recently about very specific ways git can get messed up.
To be clear, git can get messed up in many ways, but this fascinating presentation, by [Mike Street](https://www.mikestreety.co.uk/), was about just *some* of the ways we run into problems with git.

Have you ever gotten this message:

```bash
Updates were rejected because the tip of your current branch is behind its remote counterpart.
If you want to integrate the remote changes, use 'git pull' before pushing again.
```

This USUALLY means exactly what it sounds like (assuming that this message sounds like anything to you): The branch you were working on has changed on the remote, and before you push your changes to the remote, you should pull the new changes to your computer and integrate them, otherwise you might break something.

But how does git know that something has changed at the remote? Git does this by comparing commit hashes, the 40-character strings that uniquely identify a specific commit.

As I think I understand it, your git talks to the remote git and says, essentially, hey, I've got `develop` here, and before I made my changes, it had the hash `abc123`.

![a simplified git diagram](/assets/git1.svg)

And remote git (on github or elsewhere) says, "Cool, yeah, `develop` was at abc123 last time you pushed, so let's go ahead and add your changes `def456`."

![a slightly less simple git diagram](/assets/git2.svg)

But let's say your coworker updated `develop` while you were working.

![now you're in the soup!](/assets/git3.svg)

Now `develop` points to a different commit hash (now called `new-work`), and you get the above error.

However!

This comparison can only occur because git is comparing commit hashes. The hash is made up of a bunch of information, and here I quote Mike Street's presentation directly:

- the parent commit hash (or hashes, in the case of a merge)
- the commit message
- the commiter name and date of commit
- the author name and date of authorship (these can be different than the above)
- the file changes
- magic

(On a side note, if I understand this Stack Overflow answer correctly, [creating this hash involves using the SHA-1 algorithm (at least) three times](https://stackoverflow.com/a/68806436/17693068): the parent hash(es), the hash of each file that has changed, and the result of hashing the return of [`git cat-file`](https://git-scm.com/docs/git-cat-file), which is what contains the 'metadata' about the commit. And then it's all mushed together, I presume.)

The upshot of all of this means that two commits that are functionally the same: same files changed, same changes within those files, etc., can still look different to git, **because the hashes change whenever the metadata does.** So the 'updates were rejected' error can occur even when there are no true updates.

And this is why if you do:

```bash
git commit -m "do something"
git push
git commit --amend
#change the commit message
git push
```

you will get the original error message:

```bash
Updates were rejected because the tip of your current branch is behind its remote counterpart.
If you want to integrate the remote changes, use 'git pull' before pushing again.
```

The two commits are the same but git doesn't know that!

At this point, *if you are sure you are the only person working on this branch*, you could do a `git push --force` to resolve the issue. But it's better to avoid this problem in the first place, by not amending commits that have already been pushed to the remote.

We will see similar issues when rebasing (because the parent commit hash, as well as the commit date, could change).

The short version of this insight is: the commit hash updates every time the commit, **including the metadata**, changes.

Now you know!

This presentation did not fundamentally change the way I use git: the way to avoid this problem was, and remains, "do not amend commits that have already been pushed to the remote." But it did help me understand *why* this is the case. Thanks, Mike!

### Resources ###

The presentation was part of [Code and Coffee: A Virtual Coffee Conference](https://cfe.dev/events/virtual-coffee-conf-2025/). I believe that the individual talk will be posted shortly, but for now it is available as part of the livestream recording [here](https://www.youtube.com/live/EvDJpN-jJgo), starting at about the 9 minute mark.
