---
layout: post
title: My 2026 "Coding Retreat"
categories: musings
excerpt_separator: <!--more-->
description: Why and how I set up a "busman's holiday" for myself, and what I did there
---

![The "two guys on a bus" meme, where the sad guy on the left is captioned "Coding at work" and the happy guy on the right is captioned "coding on the weekend".](/assets/two_guys_on_a_bus.png)

Today, I took myself on a busman's holiday.

After a busy January and February, with all kinds of work- and non-work-related deadlines, I wanted to dig into some of the projects I'm interested in, that have no bearing on my job, that I wanted to work on.

And yes, those projects involve writing code. So yes, I wanted a vacation from work where I did the same thing that I do for money.

The two guys riding the bus meme above isn't entirely accurate, because I do enjoy my job as well, but of course there's something about working on things _just for me_ that brings me more joy. In fact, I have a [whole talk](https://www.youtube.com/watch?v=A_oU7d_H8oM) about the joy of making something that will never scale or never make any money.

So in late February I decided I needed a coding retreat, and today I was able to make that happen. I booked myself a day pass at a coworking space, in order to give myself a distraction-free zone.

These are the things I planned to work on, in this order: (roughly easiest/most fun to hardest)

- install a **responsive image plugin** for my blog, to reduce load times ([this one](https://github.com/wildlyinaccurate/jekyll-responsive-image))

- install and set up [this Python library](https://github.com/sopelj/python-ember-mug) to interact with my **Ember mug**

- finish debugging the MVP of a **Firefox extension** I've been working on (more on this later)

- add additional features to said Firefox extension

- use the Ember mug library to write a completely inane web app which will allow people to send 17-character messages to my mug

I opened my laptop at the coworking space at just about 9 in the morning with coffee in hand. I stayed until 6, with a long, restful lunch in the middle. Except for that break, I was mostly locked in, focusing on one of the above projects.

So, how did I do in those ~ 8 hours?

- **Responsive images**: What I thought would be the easiest task took nearly the whole morning; the plugin depends on `ImageMagick` which I didn't have installed and needed to build from source (twice, it turns out, because I didn't install the correct 'delegates' the first time). It's still not exactly where I'd like it to be but mobile page load times should be significantly faster now. (Edit: JK, my webserver's throwing 403s for some of the new images, which is alarming, so I went back to bog-standard images for now.) (Edit 2: All better :)

- **Ember mug**: I got blocked pretty early on when the library I installed wouldn't pair with my mug. That led me down a wormhole to eventually discover that not even `bluetoothctl` can pair with my mug, although under certain circumstances, it can at least detect that it exists. This was a bummer to discover, but there are certainly other Ember mug owners out there who have experienced the same thing and I'm confident there's a solution out there. If anyone out there has a Travel Mug 2 and has successfully paired it with a computer, drop me a line. :)

- Firefox extension: I left this in a very poor state when I had to take a break from developing it. That left me scrambling to remember what I was working on, what the state of things were, and what had (unfortunately) broken between November and now. I managed to fix most of the bugs that I found, and added some new ones (just for fun), and I think it's almost ready for release. I have some advanced features I want to add in a later version, but it's really almost ready to go out into the world.

All in all, after a long, productive day, this is what I learned:

- **I still love coding by hand.** There were a few moments where I got bogged down in tedious syntax, but for the most part, this is still fun for me. I would not have had as much fun, nor would I have bothered to book this day, if I was just orchestrating LLMs.

- **The distraction-free zone is a must for me.** If you are planning one of these, you might be able to get away with a day on the couch, or in a home office. For me, my home is a comfy place with a fridge stocked with snacks and a Nintendo Switch, and I still haven't 100%ed Hades 2. Not to mention all the procrastination laundry I could have folded. So for me, spending $20 to escape to a quiet place with nobody to talk to and no distractions was worth it, as I got significantly more done.

- **A full day is probably too long for a "retreat."** In a typical workday, my coding time is broken up by meetings, quick check-ins, and (sometimes) a quick workout, so it's easy to get through a full 8 hours. I intentionally didn't have any meetings with anyone during my retreat, and I definitely felt my energy fading as the afternoon wrapped up. If I did this again I'd probably give myself slightly more than a half day (because by the time lunch rolled around, I'd only checked off one of my five tasks) but less than a full day. And I'd build in a stretch break or two :) (My initial plan involved a complicated series of yoga classes and a massage parlor, but in the end, I decided to keep it simple, and my shoulders are telling me I made the wrong choice.)

Would I do this again? Absolutely, maybe in six months. But for now, I'm satisfied with a job well done, and now ready to take a vacation from my vacation (by going back to work).
