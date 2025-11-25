---
layout: post
title: Are There Any Good AI Documentation Apps Out There?
categories: opinions
excerpt_separator: <!--more-->
description: They haven't yet lived up to their promise.
image: /assets/broken_robot.jpg
---
![A stock-y image of a "robot" figurine, laying "dead" on the ground. Its head is a broken lightbulb.](/assets/broken_robot.jpg)

One of the places that I had hoped "AI" could be truly a time-saver is in the realm of creating documentation. There are a number of services out there, including Guidde, Scribe, and Tango, that claim that using their browser extension, you can simply perform a task while the extension records you, and then their software will describe what you did, magically creating a how-to document or video to share with your team.

The promise is amazing, but the reality is .. not so much.

The first limitation of many of these services is that you are limited to actions taken in the browser. If your task requires doing anything outside the browser, you may be out of luck. (I believe Scribe now offers a desktop app, this may be true of others as well.)

Unfortunately, the second limitation of these services is that they are all stupid.

<!--more-->

I tested two of the three services I listed in the intro paragraph on the same task: how to add a new post to a Wordpress site, using a specific custom post type with a few custom taxonomies. I will not say which two of three, but I believe them all to be the same. (If they are not all wrappers over a ChatGPT API call with maybe a slightly different prompt, I will eat my hat.)

The instructions included things like "navigate to www.google.com" when I was clearly on my Wordpress domain; "go here" instead of specific verbiage, OCR'd text that didn't know when to stop. For example, the app was supposed to see me clicking the "Log in" button and, I suppose, infer that the task was "Click log in." Instead, it wrote, verbatim: "Click "Log In Powered by WordPress Username or Email Address Password Remember Me Lost your password?"

Which, coincidentally, is the entire text content of the Wordpress login page:

![Log In Powered by Wordpress Username or Email Address Password Remember Me Lost your password?](/assets/wordpress-bad.png)
*The "Powered by Wordpress" is the alt text of the logo.*

Steps were missing, instructions, when they weren't just copying and pasting whole paragraphs of text from the page, were incorrect or garbled. Typos that I made, deleted, and fixed, were preserved whole cloth. ("Type `rkaufmna`"). And while it did manage to occasionally name specific, correct steps to take, it was often overly specific. For example, part of creating a new Wordpress post is selecting the tags or categories a post belongs to. These apps often named a literal tag or category, rather than interpreting my actions as "Choose a category that the post belongs to," which is what I had somewhat naively hoped would happen.

Okay, so what if the extension just took screenshots, and let me edit my own text to go with the screenshots? Alas, on a test recording of "adding a new post to Wordpress" there are four screenshots of the login screen and zero of how to navigate to the custom post type's Add menu. There are two duplicate screenshots labeled "Click Tags" and zero shots of what to do when you get there.

If I had to guess what's going on under the hood, the browser extension is just taking screenshots, possibly at fixed intervals, and then sending them to ChatGPT and saying "Here, describe what's in this." Of course there's no "comprehension" of what's going on, but I did expect better, for some reason?

It's a shame, because I could see a world where these extensions are aware of the browser context -- the URL at `window.location` is X, therefore the user must have navigated to X, the user clicked the third button on the page, its text content (or label) is Y... Possibly it could also track activity by the user in some way. A flurry of activity should result in more screenshots taken, and a pause in activity should imply that something less important is occurring here, and we don't need to document as thoroughly.

That would be a truly useful tool, and it seems like it's at least partially within reach with current technology. Unfortunately for these companies -- and for me, who now has to write this documentation by hand -- these ain't it.

