---
layout: post
title: Hidden Export Options in Google Slides
categories: things-i-learned
excerpt_separator: <!--more-->
description: An undocumented feature in Google Slides lets you get a spiffy HTML view.
---

To publish my slides for [Reinforcement Learning for the Math-Phobic]({% post_url 2025-01-28-reinforcement-learning-for-math-phobic %}) I had to do a lot of manual work. I cropped screenshots of the slides (and replaced some text-heavy slides with just text). I turned my speaker notes into complete sentences and interspersed them between the slides. (I was heavily inspired by how Tanya Reilly presents [her slides](https://www.noidea.dog/glue).)

So imagine my surprise when I [discovered](https://stackoverflow.com/questions/70688393/can-i-export-google-slides-as-html-in-the-drive-api) there's a hidden feature in Google Slides that can do (some of) this for me!

The menu in Google Slides allows you to choose File->Download->and a variety of formats, including PPTX, PDF, and plain text.

![Screenshot of the Google Slides export menu.](/assets/gslides-export.png)

However, if you go to the address bar, there's one more option.

A GSlides URL looks like this:

`https://docs.google.com/presentation/d/{presentation_id}/edit#slide=id.{slide_id}`

If you turn that URL into:

`https://docs.google.com/presentation/d/{presentation_id}/export/html`

then you get an HTML document that contains the slides and speaker notes on one page.

![Screenshot of what the HTML download looks like](/assets/gslides-export-html.png)

It's not perfect. The slides are output as HTML instead of images, which as you would expect, does not work well for complicated layouts, some special characters are missing, and slide animations of course are totally gone. But as a starting point, it's very helpful.

Makes me wonder what other undisclosed options are out there. [This Stackexchange post](https://webapps.stackexchange.com/questions/130654/all-google-docs-url-parameters-functions-commands) describes a number of hidden commands for Google Docs. Presumably there are a few more for Slides.

And yes, I did try `export/rtf` and `export/markdown`, with no luck. :)