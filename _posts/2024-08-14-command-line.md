---
layout: post
title: "Leveling Up on the Command Line"
categories: things-i-learned
excerpt_separator: <!--more-->
---
![I'm a hacker, ma!](/assets/imahacker.jpg)

I am _lucky_ in that my first exposure to computers was through the command line. I wasn't a wizard by any sense  when I realized that I could type "echo hi" and the computer would 'talk' back to me[\*]({{post.url}}#fn-1), but it means that I feel more comfortable in a non-GUI environment than many of my colleagues.

There's always room for improvement, though. And when I'm not at work, I'm working on a new-to-me Linux laptop. Even with [Pop OS](https://pop.system76.com/) installed, let's be real: There are some things that any Linux GUI just doesn't do that well, so the command line is still essential.

In that spirit, I bought [Efficient Linux at the Command Line](https://www.oreilly.com/library/view/efficient-linux-at/9781098113391/).

I'm only on Chapter 3 but am already learning a lot of commands that I hope to burn into muscle memory. Here are a few that I am working on now:

<!--more-->

- `!!`: repeats the previous command. I knew this one but do I remember to use it? No, because pressing up and enter is easier. However, the difference between `!!` and up-arrow+enter is that you can use `!!` anywhere in the command:

    ```bash
    $ touch forbidden.txt
    touch: forbidden.txt: Permission denied
    $ sudo !! #now it works :)
    ```

- `!grep`: this repeats the previous `grep` command, regardless of how far back in the history it is. This seems massively useful and I am going to have to remember this one.

- `!1203`: this runs the command at position `1203` in `history` and I am honestly never going to use this, but it is cool.

- `!$`: expand the final param of the previous command. For example:

    ```bash
    $ ls *.txt
    a.txt b.txt c.txt
    $ rm !$
    rm *.txt
    ```

- Reverse incremental search (aka control-R): I don't know why I don't use this more. This allows you to search through your entire command history by most recently used command that matches your input. In other words, if your history contains:

    ```bash
    git add .
    git commit -m "commit message"
    ./gradlew my-project:build
    git reflog
    ```

    and you hit control-R, then 'g': the reflog command (the magic git undo button! my favorite!) will be displayed. But if you continue typing, and next add an 'r', the command displayed (that you can run again) will be to run the gradle wrapper.

- History expansion with carets

    Oh my gosh I wish I had known about this one sooner.

    I can't think of a non-trivial example so I'll just copy the one from the book. Suppose you typed the following command:

    ```bash
    $ md5sum *.jg | cut -c1-32 | sort | uniq -c | sort -nr
    md5sum: '*.jg': No such file or directory
    ```

    (BTW, this command is a way to detect duplicate files by calculating their checksums and sorting their frequency by highest to lowest. Not something I see myself doing any time soon, but cool that this can be accomplished on the command line.)

    So if I'd typed that command above and mistyped 'jpg' as 'jg', my previous approach would have been to press up, control-A to move to the beginning of the line, and then the right arrow until I could fix my typo. Not terrible, but instead you can run:

    ```bash
    $ ^jg^jpg
    ```

    which runs the previous command, substituting the characters to the right of the carets for the characters between the carets. (This will only work on the first occurrence of the string.) This, I will admit, has truly blown my mind, and I am almost angry that nobody has shown me this before.

#### Resources

- [Some even more obscure bang-related command-line tricks](http://web.archive.org/web/20130731111822/https://craig-russell.co.uk/2011/09/28/bang-bang-command-recall-in-linux.html#.UfjygqHP32c) that are very cool to read about, but I probably will not use.
- [Fenced code blocks within bulleted lists in Markdown](https://gist.github.com/clintel/1155906) Not actually related to the command line but very relevant to the formatting of this post. Credit where credit is due.

\*<a name="fn-1"></a>We didn't have any actual games on the computer, so this was the absolute _height_ of entertainment when I was five or so.
