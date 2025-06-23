---
layout: post
title: "The Making of (and Redesigning of) BookGuessr"
categories: things-i-learned
excerpt_separator: <!--more-->
project: "Bookguessr"
description: In a list of 1000 novels, more than you think are pretty obscure.
image: /assets/bookguessr.png
---

A couple of years ago, I got into my head the idea that I wanted to make a [Wikitrivia](https://wikitrivia.tomjwatson.com/) style game with novels. I love to read, there's a lot of publicly available data about books out there, why not? I made the first prototype in a weekend, using a list of _1000 Novels You Must Read_ from The Guardian, and data from The Open Library, and it worked, but.

I didn't really want to show it to anyone because I really didn't like how it looked, or behaved, and don't even get me started on how it worked (read: didn't work) on mobile.

Recently, I got a bee in my bonnet about redesigning it. I'd take another weekend and just spiff up the CSS and be done.

Lies, all lies.

First I spiffed up the CSS. I'm not at all a designer, so this was harder than it sounds. But I used a few tips from [Erik Kennedy](https://www.learnui.design/) and I think I made it better.

![bookguessr before](/assets/bookguessr-old.jpg)
*Before*


![bookguessr after](/assets/bookguessr-new2.jpg)
*After*

Then, because the mechanic of hovering over where you want to place a book is not just mobile-unfriendly but mobile-impossible, I remade the entire site using a drag-and-drop library. I chose React-DND-kit pretty much at random, and once I figured out its quirks, I can say I'm pretty happy with it, but there may be a future blog post forthcoming about all said quirks.

_Then_, because I was running into some annoying React off-by-one bugs related to state being set when I didn't expect it, I ripped out all the game logic and redid that. (Future blog post coming: Don't store state, derive it!)

This wasn't a ton of coding work, but you know how side projects can drag on. So I'm happy to say, six months after thinking I'd just "take a weekend" to do a little cleanup, Bookguessr is finally ready for the world.

Until I get the itch to redesign it again. Which might be tomorrow.