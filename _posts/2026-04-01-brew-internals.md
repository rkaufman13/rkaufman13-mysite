---
layout: post
title: A deep dive into....homebrew's internals
categories: things-i-learned
tags: [mac, ruby, cli, incredibly useless knowledge]
excerpt_separator: <!--more-->
description: It's just a bunch of Ruby.
---

![A photo of a row of old-timey beer barrels and a tasty, half-drunk tulip glass balanced on top.](/assets/beer.jpg)

Homebrew , the Mac package manager, is something I don't think much about, because 99% of the time, it just works. The 1% of the time it doesn't is a frustrating, hair-tearing mess, but lucky for me that's rare.

I recently had to install [Amazon Corretto](https://aws.amazon.com/corretto/) v24 at work. This is the version we're being asked to use at work temporarily while we upgrade some dependencies that are blocking us from fully upgrading to Java 25.

If I had done this when 24 was the current version available, I would have been able to run `brew install corretto` without any problems. Since I hadn't, I was now in trouble. Amazon only makes long-term-stable (LTS) releases available through homebrew as well as through its [downloads](https://downloads.corretto.aws/#/overview) page, and corretto 24 is not a LTS release. So it's vanished off all public-facing documentation and download pages.

Thankfully, I was not the only person at my company to have procrastinated past the point of no return. My coworker [wrote an excellent blog post about solving this very problem](https://emmer.dev/blog/installing-old-homebrew-cask-versions/) and I followed his tutorial to install an old version of a homebrew cask.

## How to install an old version of a homebrew cask, the fast way and the slow way

If you just need to install Corretto 24 on a Mac, you should be able to follow the steps in the [blog post](https://emmer.dev/blog/installing-old-homebrew-cask-versions/) without any modifications.

Unless you are me and have in-corretto spelling (insert moray eel gif).

My silly spelling error had an upside, though, as it led me down a small rabbit hole of trying to figure out how exactly brew works, and I did learn a few things. So let's go through my coworker's tutorial together and explain what's happening at each step.

<!--more-->
Fair warning/spoiler: this post is more than 1000 words, for something that:

1. should be incredibly simple
2. is, actually, incredibly simple, but not in the sense of "just run it and it works" that I meant in #1.

Also, I'll be relying heavily on homebrew's [terminology list](https://github.com/Homebrew/brew/blob/master/docs/Formula-Cookbook.md#homebrew-terminology). I think the creators of homebrew were so committed to the theme that they forgot that most (all?) of these words do not map 1:1 to what they actually mean.

### Step 1: `brew tap --force homebrew/cask`

`brew tap` allows you to access a repository of either formulae or casks. A collection of other software, in other words. During normal operations we shouldn't need to do this, but because we want to access the full commit history of the `homebrew/cask` repo, we need to tap it. Essentially, tapping is `git clone`ing the homebrew cask repo, which can also be browsed [here](https://github.com/Homebrew/homebrew-cask).

Now we have the entire git history of the homebrew cask repo on our local.

### Step 2: `brew tap-new homebrew/local`

This initializes a new tap (an empty github repo with the correct directory structure). We're going to move a cask (instructions for how to install a precompiled piece of software) into our new tap so that brew will know how to handle it.

### Step 3: find the path of the Corretto cask's Ruby file

Christian, I hope you know this is a beautiful little two lines of bash:

```shell
$ cd "$(brew --repository homebrew/cask)"
$ git ls-files 'Casks/*' | grep -E "/corretto\.rb$"
Casks/c/corretto.rb
```

Execute the command `brew --repository homebrew/cask` (which prints the directory where that tap lives), passing the value into `cd`. Then it runs `git ls-files` in the `Casks` subdirectory and passes the result into `grep -E` (which lets us define a regular expression). [Here's a long explanation](https://stackoverflow.com/a/56242906/17693068) of what `ls-files` does, but short version, it's like `ls` but also searches git's index (which might be different from the current worktree) So this helps us locate a file in the `Casks` directory matching the regular expression. (We could also do `find . -name corretto.rb)` from the homebrew dir. It would probably be slower. Also less cool.)

### Step 4: Find the commit hash that points to version 24

```shell
$ git rev-list --all Casks/c/corretto.rb \
    | xargs -n1 -I% git --no-pager grep --fixed-strings "version \"24." % -- Casks/c/corretto.rb
51d5d6c524854fe11dfa82c5b7439e6a502c47cf:Casks/c/corretto.rb:  version "24.0.2.12.1"
a780d8ca78c3072c8c43ae6ed9108041c722fff0:Casks/c/corretto.rb:  version "24.0.1.9.1"
fe80d7e571d831942cf19f923be20db84bcd8738:Casks/c/corretto.rb:  version "24.0.0.36.2"
```

I said the previous step was beautiful, this is just wizardry. I can't even say what each part of this command does, but the end result is a list of [commit hashes]({{site_baseurl | relative_url}}{%link _posts/2025-04-28-git-commit-hash.md%}) referencing the string `version "24"`.

A much less cool way of doing the same thing might be to go to the cask repo, [find the cask file we're interested in](https://github.com/Homebrew/homebrew-cask/blob/main/Casks/c/corretto.rb), then click "History". We can see the same commit hashes there:
![A screenshot of the version history on github. Not so interesting to look at.](/assets/brew-hashes.png)

### Step 5: Move that version of the cask to our local tap

```shell
$ git show "51d5d6c524854fe11dfa82c5b7439e6a502c47cf:Casks/c/corretto.rb" \
    | sed "s/cask \"corretto\"/cask \"corretto@24.0.2.12.1\"/" \
    > "$(brew --repository homebrew/local)/Casks/corretto@24.0.2.12.1.rb"
```

Again, some impressive stuff. `git show {commit}:file` prints the contents of that file at that commit to stdout. The `sed` statement replaces `cask corretto` in the output to `cask corretto@24.0.2.12.1` and then writes it to a new caskfile in our local tap.

After doing that, all we need to do is use brew to install the new cask file:

```shell
$ brew install --cask homebrew/local/corretto@24.0.2.12.1
```

BUT!

Let's say we made a silly error like spelling `corretto` wrong. It would be nice to understand the big picture. And to my surprise (actual surprise), the actual big picture, if you look at all the steps above, is "find, then move to the correct place on your computer, the correct version of a 24-line Ruby file." That's it.

This is the contents of that file:

```ruby
cask "corretto" do
  arch arm: "aarch64", intel: "x64"

  version "24.0.2.12.1"
  sha256 arm:   "94ec00147ab39f1a3c06050da8ed274fa2d9aed1dd94d154b8db2710a061c6bb",
         intel: "b2317bda88049adee74f402d7ffd1d5940b8a01355b8105324908c396d681476"

  url "https://corretto.aws/downloads/resources/#{version.sub(/-\d+/, "")}/amazon-corretto-#{version}-macosx-#{arch}.pkg"
  name "AWS Corretto JDK"
  desc "OpenJDK distribution from Amazon"
  homepage "https://corretto.aws/"

  livecheck do
    url "https://corretto.aws/downloads/latest/amazon-corretto-#{version.major}-#{arch}-macos-jdk.pkg"
    regex(/amazon[._-]corretto[._-]v?(\d+(?:\.\d+)+)[._-]macosx[._-]#{arch}\.pkg/i)
    strategy :header_match
  end

  pkg "amazon-corretto-#{version}-macosx-#{arch}.pkg"

  uninstall pkgutil: "com.amazon.corretto.#{version.major}"

  # No zap stanza required
end
```

To my utter astonishment, and this is not an exaggeration, when I removed the placeholders from the URL on line 8 and popped [https://corretto.aws/downloads/resources/24.0.2.12.1/amazon-corretto-24.0.2.12.1-macosx-aarch64.pkg](https://corretto.aws/downloads/resources/24.0.2.12.1/amazon-corretto-24.0.2.12.1-macosx-aarch64.pkg) into my browser, a file downloaded. And when I double-clicked that file to install it, I had Java 24 on my computer.

All I had to do after that was run `/usr/libexec/java_home -V` (which lists all JVMs installed) and then set my environment variables to point at the version 24 installation. Ta-da!

Not all cask files are this small, but they're all roughly this simple. I started poking around, and it seems that some of them have more detailed uninstall scripts (the "zap stanza"), others, especially fonts, list a [truly eye-popping number of files](https://github.com/Homebrew/homebrew-cask/blob/51d5d6c524854fe11dfa82c5b7439e6a502c47cf/Casks/font/font-n/font-noto-nerd-font.rb) (all those font variations!), yet others have OS dependencies. These bits are called stanzas; [the common ones are listed here under "Stanzas"](https://docs.brew.sh/Adding-Software-to-Homebrew#casks) and the [weird/uncommon ones are here](https://docs.brew.sh/Cask-Cookbook#optional-stanzas). But it's all just Ruby all the way down. This shouldn't be a surprise; I'm sure most package managers look like this when you really get down to it, but, well, I was surprised.

Manually downloading and installing Java rather than using brew's infrastructure has a downside, which is that we won't be able to upgrade this install of Corretto from within brew. But I don't mind; I'll just switch back to using brew once we get the go-ahead to move to a new, actually-available LTS release.
