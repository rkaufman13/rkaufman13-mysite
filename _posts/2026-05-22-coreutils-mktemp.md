---
layout: post
title: "30 Days of Coreutils: mktemp"
categories: things-i-learned
tags: coreutils bash cli
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: One I never thought I'd use, until I did.
---

{% include coreutils-header.html util="mktemp" %}

`mktemp` makes a temporary file on your computer. This is not something I thought I would ever use (its main use cases are for scripts to have temporary scratch pads to write on), but then I came across [Mist](https://mist.inanimate.tech/).

Mist is a super cool Google-Docs-like experience for temporary Markdown files. Drag a markdown file into the browser and it becomes collaborate-able to anyone with the link for the next 100 hours. Hit download, and you now have a copy of that doc. I am very excited about the potential for using this and I plan to share it with everyone I know.

You can also upload an existing doc to Mist via cURL, with `curl https://mist.inanimate.tech/new -T file.md`

This is all well and good, but I wanted to be able to create a blank doc from the command line. (Yes, you can create a blank doc from the browser with one click. I don't care. :))))

The obvious answer is to write a script that executes:

```bash
#!/bin/bash
touch file.md
curl https://mist.inanimate.tech/new -T file.md
```

But what if file.md exists? Ok, let's give it a file name as an arg.

```bash
FILE = $1
touch $FILE
curl https://mist.inanimate.tech/new -T $FILE
```

Then I could execute `new_md mydoc` , which would create a new file with the name `mydoc`, and immediately upload it to Mist. But what if `mydoc` already exists? Plus, if I upload a doc named `mydoc.md` and then re-download it from Mist, Mist gives it a random name anyway. So the name of the OG blank document does not matter, because the one that is downloaded, if it is, will have a different file name. Wouldn't it be great if we could know that the original document--that's only used to open a new doc on Mist-- was guaranteed to have a unique file name, and that it would erase itself in time?

Enter `mktemp`.

As stated, `mktemp` creates a throwaway file with a random filename, and then outputs the random filename. So I can do:

```bash
function create_new_doc(){
FILE=$(mktemp)
curl https://mist.inanimate.tech/new -T $FILE | tee /dev/tty | pbcopy
}
```

The `tee /dev/tty | pbcopy` ensures that the resulting URL is both output to STDOUT and copied to my clipboard for easier use. (I could also have just done `|pbcopy|pbpaste`. These utils are Mac-only, but [there's a few aliases you can use on Linux.](https://superuser.com/questions/288320/whats-like-osxs-pbcopy-for-linux)).

`mktemp` accepts a handful of args. `-d` creates a temporary directory instead of a file, and `-p` lets you specify a different directory than default for the temporary file to be created. Since the default tempdir will be automatically cleaned up, but other directories probably won't be, this turns `mktemp` into something less than temporary.  `-t` lets you define a file naming template, but it's super finicky.

The man page says:

```bash
-t interpret TEMPLATE as a single file name component, relative to a directory: $TMPDIR, if set; else the directory specified  via -p; else /tmp [deprecated]
```

Elsewhere, it says: `TEMPLATE must contain at least 3 consecutive 'X's in last component.`

Neither of these sentences made absolutely any sense to me until I started playing around with it, but essentially if you provide a TEMPLATE either as an inline arg or with the `-t` flag, IF it is in the right format, you can get a file with that name. The "right format" in this case means at least one character that is not the letter 'X', then at least 3 'X's, then, optionally, an extension.

```bash
$ mktemp tXXX
tgBE
$ !!
twH2
$ !!
tFmv
$ mktemp temporary-file-with-a-randomly-generated-name-XXXX.txt
temporary-file-with-a-randomly-generated-name-YG7k.txt
```

Why you would want this option, I'm not sure. But you should use Mist. I wish I'd come up with it.
