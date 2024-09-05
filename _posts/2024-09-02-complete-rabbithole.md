---
layout: post
title: "In Which I Go Down a Complete Rabbithole About Bash Completion"
categories: things-i-learned
excerpt_separator: <!--more-->
description: Ever wonder what is actually going on in your shell when you type, for example, `cd ~/myp`, hit `<TAB>`, and the shell completes `~/myproject`? Oh yeah, definitely not me either.
image: /assets/rabbit_on_computer.jpg
---

![It's the rabbithole I went down. Get it?](/assets/rabbit_on_computer.jpg)

Ever wonder what is actually going on in your shell when you type, for example, `cd ~/myp`, hit `<TAB>`, and the shell completes `~/myproject`?

Neither had I, until recently.

This was supposed to be a post about the next chapter of Efficient Linux at the Command Line, which is about navigating the file system. However, the author dropped in the idea of the bash builtin `complete` in a sidebar, and I might have gone a little off the deep end. 

In the source code given for writing a custom bash function, the last line added to the user's config file is: `complete -W "work recipes video beatles" qcd` which would mean if someone typed `qcd` followed by two tabs, the terminal would print all the available keys: in this case `work` `recipes` `video` and `beatles`.

What _is_ this? What's going on here?

If you type `complete` by itself, you get a very long list of what looks like nonsense:

```bash
complete -F _longopt mv
complete -F _root_command gksudo
complete -F _command nice
complete -F _longopt tr
complete -F _longopt head
...and so on
```

This is, it turns out, a list of what completion command is run when you run one of the bash commands at the end of each line. In other words, `complete -F _longopt mv` means, if you type `mv <tab><tab>` complete will run the function (`-F`) `_longopt`.

`_longopt` and the other built in completions are very long bash functions that mostly call other functions, and if you want to spend a lot of your next three-day weekend retracing my steps, you are welcome to it. For the purposes of this post, however, I'll talk about an overly simplified completion, because I already spent more time on this Labor Day weekend reading about this than I ever imagined I would.

<!--more-->

Via this [2009 Linux Journal article](https://www.linuxjournal.com/content/more-using-bash-complete-command), which my dad would probably be kvelling to know I read, here's an example:

```bash
$ # Create a dummy command:
$ touch ~/bin/myfoo
$ chmod +x ~/bin/myfoo

$ # Create some files:
$ touch a.bar a.foo b.bar b.foo

$ # Use the command and try auto-completion.
$ # Note that all files are displayed:
$ myfoo <TAB><TAB>
a.bar a.foo b.bar b.foo
```

Now we could add this line to our `~/.bash_profile` (or `~/.bashrc` etc) file:
`complete -F _mycomplete_ myfoo`

Hey, that kind of looks like the lines from running `complete` before! Except we need to define `_mycomplete_` ourselves. We'll put it in our config file as well, and we'll say that `myfoo` can only handle `.foo` files, so we don't want to autocomplete any filenames that have other extensions.

```bash
function _mycomplete_()
{
    local word=${COMP_WORDS[COMP_CWORD]}
    local xpat='!*.foo'
    COMPREPLY=($(compgen -f -X "$xpat" -- "${word}"))
}
```

It's that simple. First we define a local variable, `word`, and initialize it to the current word being typed. (`$COMP_WORDS` is an internal variable holding all the words in the current line, as an array, and `$COMP_CWORD` is an index to the current word.) Then we define a pattern we want to exclude -- in this case, the pattern will exclude anything that doesn't match `*.foo`. (Regular regex syntax here.) `COMPREPLY` is how we tell bash to actually respond, and it calls the `compgen` function (another builtin) to generate a list of files in the current directory (`-f`) and exclude everything that doesn't match the pattern specified. Then finally we pass in the current word so that only items that do match it are returned, giving us:

```bash
$ myfoo <TAB><TAB>
a.foo b.foo
```

or:

```bash
$ myfoo a<TAB>
a.foo 
```

What if your `myfoo` command takes options, like: `--version` or `--help` or `--super-foo`, and you want to display those options to the user? You could:

```bash
function _mycomplete_ (){
#omitted for brevity
 if [[ ${word} == -* ]]; then
    # complete the "--" parameters
    local opts="--help --version"
    COMPREPLY=( $( compgen -W "$opts" -- "${word}" ) )
 else
    COMPREPLY=($(compgen -f -X "$xpat" -- "${word}"))
 fi
}
```

Now you can do:

```bash
$ myfoo <TAB><TAB>
a.foo b.foo
$ myfoo --<TAB><TAB>
--version --help --super-foo
```

To see all the builtin completion functions and _really_ go deep like I did, you have a couple options: Various sources told me to look in either `/etc/bash_completion.d/` or `/usr/share/bash-completion/`, neither of which had what I was looking for on my flavor of *nix. (I'll try on my work Mac tomorrow, just for `complete`ness's sake. Sorry.) But `declare -f grep _longopt -A 50` (for example) gets you all the gory details. Happy complete-ing!

### Resources

- [Long, helpful blog post about custom complete commands](https://www.benningtons.net/index.php/bash-completion/)
- [Bash builtin complete functions, variables, and another line-by-line walkthrough of a custom command](https://devmanual.gentoo.org/tasks-reference/completion/index.html)
- [2009 Linux Journal article on completions](https://www.linuxjournal.com/content/more-using-bash-complete-command)