---
layout: post
title: "A Handy Shell Script to Publish Jekyll Drafts"
categories: things-i-learned
tags: jekyll bash
excerpt_separator: <!--more-->
---

![Randall Munroe as usual nails it.](/assets/automation_2x.png)
*[xkcd](https://xkcd.com/1319)*

The quest to remove friction from posting to this blog continues. In an earlier post, I [shared how I used rake to automatically generate a blog template for me and place it in Jekyll's drafts folder]({{site.baseurl}} {% link _posts/2025-07-12-rakefiles.md %}). Now, I realized I'd also like to handle publishing that post with approximately 10% fewer keystrokes.

I'll share the script first, then explain my motivations and how it works.

```bash
#!/bin/bash
PS3="Choose a draft to publish: "
select FILENAME in _drafts/*;
do
    today=$(date -I)
    shortfile=$(basename $FILENAME)
    mv $FILENAME _posts/$today-$shortfile && echo "Successfully moved" || echo "Had a problem"
    break
done
exit
```

That's it, that's literally it, but I'm so excited about it.

Jekyll considers a post to be a draft if it is a markdown file in its `_drafts` folder. It considers it to be published if it is in its `_posts` folder. I believe the filename in `_posts` also needs to contain the date (e.g. `2025-11-19-this-is-a-post.md`) but I'm not sure if that's a hard requirement or just a requirement for my setup.

So what I have to do when I publish a new post is `mv _drafts/mydraft.md _posts/yyyy-mm-dd-mycoolpost.md` and that is clearly too many keystrokes, right? Now I just have to write `rake publish` (I created a rake task that just runs this script), choose my file from a list of files, and I'm done.

To write this I had to learn about two new-to-me bash concepts, the `select` construct and `basename`.

### The `select` construct

`select` can be used to create (super basic) menus. The [man page for `select`](https://man7.org/linux/man-pages/man2/select.2.html).....is for the wrong thing! But [a good writeup on the select construct can be found here](https://linuxize.com/post/bash-select/). In short, `select thing in list` will pop up a menu that you can interact with by choosing the item number, and assign the value to the variable `$thing`.

You can do: `select option in "BLT" "cheesesteak" "pb&j"` and you'll get the following output:

```bash
1) BLT
2) cheesesteak
3) pb&j
$>
```

In the case of my script, the "in" is the contents of the directory `_drafts/*`. 

(Notice the syntax is not `in ls _drafts/*`, implying that we're not just executing a command and passing the results to the select construct. Which is a mystery for another time.)

The upshot, however, is that I get a list like:

```bash
1) _drafts/ai-is-hard.md            3) _drafts/microblogging.md         5) _drafts/recipe-buddy-part1.md
2) _drafts/efficient-linux-ch-4.md  4) _drafts/rake-publish.md
```

(oooh, a peek behind the curtain!)

`select` will then allow you to choose one of the numbers, and store the value in the variable we defined (here, `$FILENAME`.)

It will continue to loop until it reaches a `break` command, so the break is important in this script. But then all we need to do is get today's date and rename/move the file to its new home.

### `basename`

This is a lil one, but a handy one. Again, let's go to the [man page](https://man7.org/linux/man-pages/man1/basename.1.html) for this util:

`BASENAME -  strip directory and suffix from filenames`

Does what it says on the tin. If you have `/home/user/long/path/to/file.md` and you want `file.md`, `basename /home/user/long/path/to/file.md` will get that for you. Note that it removes the extension if and only if the extension is provided as a second argument, and if the provided extension matches that of the file, which is a little quirky. In my case I want to keep the extension, so this works well for my use case.

And there you have it, 10 lines of code that took longer to write about than to write, and which will surely save me ~~hours~~ ~~minutes~~ *seconds* of precious time. Huzzah!
