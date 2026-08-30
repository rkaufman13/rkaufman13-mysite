---
layout: post
title: "My First Reveal.js Plugin: Image Credit Generator"
categories: useful-things
excerpt_separator: <!--more-->
project: "Reveal.js tweaks"
description: The first of many.
---

![An image of a power plug. It is not plugged in to anything, but it's still a plugin. Sort of.](assets/2026/plug.jpg)
*A "plugin". Photo by Markus Winkler on Pexels*

I really, really like Reveal.js for creating presentations. It's flexible, beautiful out of the box, and infinitely easier to tweak than, say, Google Slides. For example, before I gave [React at 60 FPS]({{site.baseurl|relative_url}}{% link _posts/2026-05-21-react-60fps-slides.md%}) for the first time, I got feedback like, the day before I was scheduled to give it, that the theme didn't match the content. I was able to swap out all the backgrounds, colors, and fonts in about 10 minutes.

But this isn't a love letter to Reveal. Instead, I want to share that I've released a plugin for Reveal.js - my first, but not my last.

This plugin solves a problem that I didn't realize I had, until recently. When using images from sources that require (or request) credit, I don't necessarily want the credit to take up a lot of slide real estate. I might not even want the credit on the same slide at all, as it can be distracting! (We could also put it in a very small font, or write the credit [sideways on the right of the screen](https://github.com/rschmehl/reveal-plugins/tree/main/attribution), but I've been to enough presentations that are hard to read from the back of the room to know I don't want to do that.)

My solution is [RevealJS-image-credits](https://github.com/rkaufman13/revealjs-image-credits), a plugin that collects all the image credits throughout a presentation and writes them to a location of your choosing (the final slide, for example).

I explain it below (taken from the plugin's readme):

> After initialization, add image credits to any `<img>` tags in your presentation with the `data-credit` attribute.
>
> `<img src="photo_of_me.jpg" data-credit="Photo by the author"/>`
>
> `<img src="Barack_Obama.jpg" data-credit="Wikimedia Commons"/>`
>
> You can even do HTML crimes:

> `<img src="photo-with-a-cc-by-license.jpg" data-credit="Photo by a person whose image terms require me to link to their <a href='https://neocities.org'>website</a>">`
>
> Then, anywhere in the presentation, add a div with the id #photocredits. The plugin will automatically populate the credits by page number, like:
>
> 0: Photo by the author
>
> 2: Wikimedia Commons
>
> 4: Photo by a person whose image terms require me to link to their [website](https://neocities.org)
>
> The div is unstyled, but you may of course style it to match your presentation.

By adding the image credit information to the img tag itself, the credit "stays with" the image, even if it's moved to a different slide, and by rendering the `#photocredits` div dynamically, the page numbers are always accurate.

See a [live demo](https://rkaufman13.github.io/revealjs-image-credits/demo.html) on Github and of course let me know what you think! The plugin itself is a single script with no dependencies, and so it should be infinitely modifyable as well.
