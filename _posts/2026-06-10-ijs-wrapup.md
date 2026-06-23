---
layout: post
title: iJS San Diego 2026, Wrapped
categories: things-i-learned
excerpt_separator: <!--more-->
description: The talks I loved (and the talks I gave) at the International Javascript Conference.
---

![A vintage postcard that reads "Greetings from San Diego" and depicts palm trees, beaches, and Mission-style buildings.](/assets/san_diego.jpg)

As I have [previously written]({{site_baseurl | relative_url }}{% link _posts/2026-06-07-coreutils-wrapup.md %}), I was invited to speak at iJS San Diego in early June. I talked about the lessons I learned working on a side project that involved a lot of animations in React. The talk went well, and afterward [Mark Erikson](https://blog.isquaredsoftware.com), the creator of Redux Toolkit, who was sitting in the back and laughing at a handful of my jokes, told me how much he enjoyed it. I felt (and still feel) like I met a celebrity.  So that was very neat.

The rest of the conference was admittedly a bit of a blur, both because I had been nervous leading up to the talk and was sort of mentally bouncing off the walls afterward, but also because I could only stay for the first day due to un-movable commitments back home later that week. But I did manage to attend a few great presentations.

The first was [Gil Fink](https://gilfink.medium.com/)'s discussion of the JS event loop and the new Scheduler API. The event loop is something I've had to learn about through trial and error so it was great to get such a clear explanation, with very clear code examples (that are unfortunately not available online as far as I am aware).

However, if you are interested in the Scheduler API portion of the talk, I think if you read [this blog post](https://gilfink.medium.com/task-management-in-javascript-8be9e71fcb3d) of Fink's you will get a small sense of what the talk was about. In short, the new API (available in all major browsers except Safari, and there's a decent polyfill available) lets you break up compute-heavy tasks so as to not block the main thread. With `scheduler.yield()` you can essentially "check in" on a long-running task (say by a simple `if i %1000 ==0` check), giving the browser a microsecond to run any other pending tasks, before going back to the long task. And `scheduler.postTask` lets you add tasks with a specific priority set, so if you know something can run with a lower priority, you can assign it the priority of `'background'` and it will run after tasks with a `'user-blocking'` or `'user-visible'` priority.

I am looking forward to thinking about how to try this out at work. I don't know that there is an obvious place to slot it in, but I'm keeping the technique in mind for the future.

The second great talk was by Mark Volkmann, a very expressive, energetic speaker talking about [wrec](https://github.com/mvolkmann/wrec), the web component library he has created. 

Last year in early March, I attended a talk about web components which was my first time hearing about them. Now, a year and a half later, I've heard about them enough to think it's something I want to play around with. Volkmann's library, `wrec`, is , I think, meant to feel like React (`wrec` apparently stands for `Web REactive Components`) but of course with less boilerplate and no build process.

`Wrec` isn't perfect to me - it uses classes rather than functional components, and I've always thought Javascript's class implementation is a little half-baked. And the implementation of context is a little, I am sorry to say, janky. However, as a new library that seems to be actively maintained by someone who cares a lot about minimizing boilerplate and maximizing readability, I'm confident that if these issues can be fixed, they will, or that I'll learn to not care as much. :)

The slides are available on [github](https://github.com/mvolkmann/talks/blob/master/wrec.key.pdf) and `wrec` can be installed via npm. I'm looking forward to trying it out.

All in all, it was a great conference. I'm grateful to Devmio for having me, and hope to come back next year.

