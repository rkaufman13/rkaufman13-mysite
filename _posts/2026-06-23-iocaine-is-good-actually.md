---
layout: post
title: Iocaine (the AI scraper poisoner) is Good, Actually
categories: things-i-learned
excerpt_separator: <!--more-->
description: The "deadliest poison known to AI" is very easy to set up. You should.
---

![Prince Humperdinck, from The Princess Bride, right after he's smelled (somehow) the odorless iocaine powder used to kill Vizzini.](/assets/2026/humperdinck-iocaine.jpg)

Wikipedia recently announced that it is blocking 2 billion bot visits per day. Somewhere between [a third](https://radar.cloudflare.com/traffic?dateRange=52w#bot-vs-human) to [half](https://www.cnbc.com/2026/03/26/ai-bots-humans-internet.html) of all the traffic on the Internet is bots, and most of those bots are AI crawlers.

Since as far as I can tell [pay-per-crawl](https://blog.cloudflare.com/introducing-pay-per-crawl/ ) is dead[^1] it behooves the owner of a website to try to stop the bots from crushing it.

And a simple `robots.txt` isn't going to do it. One redditor wrote: "OpenAI alone can crawl more than 500k a day. Hammering our robots.txt 140k a day as if it might change every second." That's absolute madness.

I did some research, and two options are very promising: [Anubis](https://anubis.techaro.lol/) and [Iocaine](https://iocaine.madhouse-project.org/). Spoiler, I eventually ended up setting up Iocaine, but let's talk about them both.

## Anubis

Anubis is a "web AI firewall utility that weighs the soul of your connection" using a proof-of-work challenge. Without the Egyptian mythology, it's a reverse proxy which intercepts HTTP requests and forces your browser to do a little Javascript challenge before accessing the content. Most (not all) AI scrapers can't execute JS, so they can't get past the challenge.

The [docs](https://anubis.techaro.lol/docs/category/environments) are very thorough but I also found this [random Malaysian ham radio operator's blog post explaining how it works and how to set it up](https://hamradio.my/2025/07/how-anubis-works-fighting-bots-with-proof-of-work/) very useful.

Mostly, it just works. Human users (may) see a brief splash screen, which might annoy people. Unless you pay for the [unbranded version](https://anubis.techaro.lol/docs/admin/botstopper), the splash screen features a cute catgirl, which might not be everyone's cup of tea. (The unbranded version is only $50/mo which should not be a blocker for 'real' companies.)

## Iocaine

The other promising tool I looked into, and ultimately decided to use, is [Iocaine](https://iocaine.madhouse-project.org/).

Unlike Anubis, its goal is not to block scrapers but to trap them in an [infinite maze of garbage](https://poison.madhouse-project.org/). If it detects that a scraper is accessing the page, it feeds it a completely different page of nonsense text, with a few links that lead to other pages of nonsense text, and on those pages there are more links...a scraper could really waste a lot of time in this maze of twisty passages, all alike.

Among its advantages: 

No splash screen.

Is not just a blocker for bots but actively poisons them.

Is called Iocaine.

![The Princess Bride's "Man in Black" (obviously Wesley, why is Buttercup so stupid) toasting as he drinks a glass of wine poisoned with iocaine.](/assets/iocaine.jpg)

It does rely (partially) on the user-agent header being set correctly. The 'good' crawlers are already doing this and being turned away at, say, the Cloudflare level, for anyone who has Cloudflare's bot protection turned on. The bad ones will blow right past this maze, which is why Iocaine has a few other detection methods which I don't fully understand.

That said, it is catching a surprising amount of traffic. More on that later.

It is fairly easy to set up, following these [instructions](https://iocaine.madhouse-project.org/documentation/3/getting-started/). If you were now to curl my site:

```bash
$ curl https://www.readwriterachel.com
```

you would receive the HTML content of the page.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Rachel Kaufman, developer</title>
  <meta name="description" content="I&#39;m a full-stack developer. I build web apps in Java, Javascript, and Python.">
  ....
```

But if you were a bot (which would [put a damper on our relationship](https://getyarn.io/yarn-clip/25c30f44-e0de-4388-b234-e8b49d088a28)):

```bash
$ curl https://www.readwriterachel.com -A Perplexity
```

You would receive something entirely different.

```html
<!doctype html><meta charset=utf-8><meta content="width=device-width,initial-scale=1.0" name=viewport><title>Time of life had been impossible even.</title><body><main><h1>Time of life had been impossible even.</h1><p>It. From time to learn from past mistakes. It need hardly be back before five. Which leaves us seven hours." He could hear and feel.<p>(GOOD, GOODER, GOODEST), ir- regular forms and the like — to ar- rest the course of the twentieth century. With the girl out of the way), John raised objections. "But aren't you all in one hundred and forty different girls in.
....
```

It uses Brave New World and 1984 as source text for the gibberish, because of course it does. (This can be customized with any text source, so why not throw in a copy of [Dune: The Butlerian Jihad](https://en.wikipedia.org/wiki/Dune%3A_The_Butlerian_Jihad) for good measure?)

Seriously though, setting this up was so easy. Not painful at all.

![The "man in black" saying "Life is pain, highness."](/assets/life-is-pain.gif)

That said, we should make two changes that are not included in the basic setup instructions.

First, I did notice that certain infinite garbage pages were [being indexed by Google](https://www.google.com/search?q=bash+site%3Areadwriterachel.com). While that's funny, it's also not quite what I wanted. According to [this issue](https://git.madhouse-project.org/iocaine/iocaine/issues/131), this is a feature, not a bug, but we can allow the bots we want through by updating our iocaine config, adding a drop-in file, like so:

```bash
declare-handler default {
    trusted-user-agents Googlebot bingbot
}
```

I added `ia_archiverbot` as well after reading that the Internet Archive is being [blocked by major news sources even as it's being hit by scrapers just as much as the rest of the Internet](https://www.wired.com/story/the-internets-most-powerful-archiving-tool-is-in-mortal-peril/). This blog is not exactly a major news source, but I'm doing my part!

When I set this up, I expected that this effort would feel really good, but not "do" anything,  since, again, Cloudflare is _supposed_ to block known bad scrapers.

I sure was surprised. After enabling iocaine, my site is receiving more traffic than ever, according to nginx access logs. By orders of magnitude. This is actually bonkers, and probably not in fact the ideal outcome, but I'm keeping it on for now. (I assume this is because there are unknown bad scrapers that are sneaking through Cloudflare's firewall, not some other sinister explanation.)

The second recommendation I have is to cap the amount of memory Iocaine uses. It doesn't use a lot, but just to be safe, we can set some sensible defaults.

With systemd as our service manager, it's quite easy. In the setup instructions, when we get to using `systemctl edit iocaine.service` we can simply add these lines:

```diff
[Service]
ExecStart=/opt/iocaine/bin/iocaine --config-path /opt/iocaine/etc/iocaine/config.d start
+MemoryHigh=32M
+MemoryMax=35M
```

to the existing suggested config.

This has the expected effect of limiting Iocaine to that much memory on the machine. I started with about half that and it kept OOMkilling itself, so I wouldn't go much lower than 32 MB.

There are some folks saying that Iocaine isn't really useful for static sites, because replacing one HTML file with another isn't the same efficiency gain as replacing multiple trips to a database, API calls to one service or another, etc., with a static HTML file. That's fair. But this feels like, in some way, I'm gaining back a tiny bit of the control that AI companies have taken away from me. And that feels good.

![Westley's famous "as you wish" scene.](/assets/asyouwish.gif)

[^1]: I spent a lot of time searching for people who like pay-per-crawl and have actually made money off it. It's been out for a year, surely there's at least one success story? But nah, after the initial wave of hype...crickets.
