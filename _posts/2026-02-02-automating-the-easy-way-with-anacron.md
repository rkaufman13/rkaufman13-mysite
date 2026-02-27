---
layout: post
title: "Automating Stuff the 'Easy' Way With anacron"
categories: things-i-learned
tags: bash linux
excerpt_separator: <!--more-->
description: Why use cron or launchd when you can do something even more complicated?
---

![Dali's famous "melting clocks" painting, "The Persistence of Memory." Melty, soft clocks litter an otherwise apocalyptic landscape.](/assets/The_Persistence_of_Memory.jpg)

`cron` is a wonderful tool for running tasks on a schedule. Set it once, and then forevermore on your schedule, `cron` will handle repeatedly doing the thing.

Unless your computer is off! `cron` was originally designed for mainframes that never are turned off. If you have a task scheduled to run every day at midnight but your laptop is closed every night, `cron` will never run the task.[^1]

I recently learned about `anacron` , which solves this problem by running things at a "scheduled-ish" time. Instead of specifying a time, you specify a frequency (hourly, daily, weekly, etc). When anacron starts (when your computer wakes from sleep/etc) if it's been more than the specified time since it last ran, it runs. Simple, right?

Eh, not so much. Possibly because I had some complicated things I wanted to set up, getting everything aligned and working took almost a week (admittedly because I was waiting for `anacron` to run and wasn't interested in force-scheduling it).

My main problem was that I wanted `anacron` to run as me, rather than as root. By default, unlike `cron`, `anacron` only runs as root.

I wanted to set up `urlwatch` to keep an eye on some websites, using headless Chrome. Automatically hitting a website as root seems like not a great idea? So running as a non-superuser seemed like the way to go.

Here's what I did:

## Setup

First, get `anacron`. If you have a Red Hat system, you already have it as part of `cronie`. On Ubuntu-based distros, you may have to install it. On a Mac, there is no official support for `anacron` and you are recommended to use `launchd`. On the other hand, [there's this Macports option with all of 12 installs](https://ports.macports.org/port/anacron/) 😬 which I probably will not be trying.

Then, I followed the steps [in this Opensource.com article](https://opensource.com/article/21/2/linux-automation) to configure `anacron` to run as my user. To summarize that article in my own words:

- Create a test script to practice on.
    My example script looked like this:

    ```bash
    #!/bin/bash
    echo $(whoami) >> ~/dontyouknowwhoiam.txt
    ```

    This should prove that anacron is running as me (which I still wasn't 100% confident of until testing it).

- Create local directories that we'll point `anacron` to instead of the system directories:

    ```bash
    mkdir -p ~/.local/etc/cron.daily ~/.var/spool/anacron
    ```

- Create a *local* configuration file at `/.local/etc/anacrontab`:

    ```bash
    SHELL=/bin/sh
    PATH=/sbin:/bin:/usr/sbin:/usr/bin #replace with your full $PATH. anacron doesn't have access to system environment variables set in, say, ~/.profile.
    1  0  cron.mine    run-parts /home/{user}/.local/etc/cron.daily/
    ```

    This will run everything in the `~/.local/etc/cron.daily` folder every 1 day, waiting 0 minutes after the computer starts up. The buffer can be helpful if you're running heavy scripts, I assume. The `mine` is an arbitrary string to distinguish from `cron.daily` or `cron.weekly` etc.

    As an aside, `anacrontab` is a perfectly logical name for the scheduling file belonging to `anacron`. `cron` has a `crontab` (short for cron table), and so `anacron` has an `anacrontab`. But for an elder millennial like myself, this was inevitable:

    ![Sir Mix-a-lot overlaid with meme text saying "My anacrontab don't want none"](/assets/anacrontab.png)

    I'm so sorry. (Not really)

- Tell our computer to run `anacron` on a schedule. The article suggests adding this line to your `~/.bash_profile`:

    ```bash
    anacron -t /home/{user}/.local/etc/anacrontab -S /home/{user}/.var/spool/anacron
    ```

    This manually triggers `anacron` with the local anacrontab, and use your local spool file (which is what `anacron` uses to keep track of the last time it ran). Putting it in your ~/.bash_profile means that `anacron` will check for new jobs every time you restart your computer.

    Putting it in ~/.bashrc (or sourcing the profile file from rc) will run it when you open a new terminal window. Finally, putting it in your `crontab`:

    ```bash
    0 0 * * * anacron -t /home/rachel/.local/etc/anacrontab -S /home/rachel/.var/spool/anacron
    ```

    means `anacron` will also check for new jobs at midnight, in case your computer hasn't been off. I used all three options, because what's the harm. Worst case, anacron decides that it hasn't been long enough since it last ran and goes back to sleep.

Those are the basic steps. That said, I ran into at least one bump on the road to better automation.

It's not stated anywhere but the man page, but`run-parts` has fairly specific naming requirements for executables, for it to run them. In default mode, according to the man page,  

>the names must consist entirely of ASCII upper- and lower-case letters, ASCII digits, ASCII underscores, and ASCII minus-hyphens.

You can check that `run-parts` is happy with `run-parts --test /home/{user}/.local/etc/cron.daily`.

Then I had to get `urlwatch` up and running. I'm going to save that for a separate post, because (as usual) I've gotten a little verbose. Up next (eventually): how to configure `urlwatch` to check for changes to websites on a schedule!

[^1]: Unless your laptop is like mine and "forgets" to sleep when the lid is closed, which is a whole other hilarious problem.
