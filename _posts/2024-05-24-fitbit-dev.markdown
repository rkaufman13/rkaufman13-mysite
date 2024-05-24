---
layout: post
title: "Developing for the Fitbit Versa"
categories: things-i-learned
excerpt_separator: <!--more-->
---

In my previous post I said something about learning Android app development so I could make a Fitbit app. However, silly me-- just because Google owns Fitbit now does not mean that Fitbits run Android. (:

Android Wear is what powers Google-owned smartwatches, but if you have a vanilla Fitbit like I do, it's Fitbit OS. Clear as mud. The upshot, however, is that if you want to write an app for Fitbit OS, you can use plain ol' Node. So that's what we'll do today.

[Fitbit's dev page](https://dev.fitbit.com/getting-started/) has a good tutorial which we'll follow. First, make sure you have node installed, and have downloaded the Fitbit simulator. (Links on Fitbit's page.) Then, run `npx create-fitbit-app my-app` to get started. For this blog post I'm following Fitbit's instructions so the prompts to answer are clock, any name, no companion.

`cd` into your newly created directory.

I'm developing this app for my personal use (for now) and my Fitbit is a Versa 2, running the "mira" version of Fitbit OS. The default settings for `npx create-fitbit-app` assume I have at least a Versa 3. To get my new app onto the Versa 2 simulator (and ultimately onto my wrist) I have to edit my package.json:

```json
"devDependencies": {
-    "@fitbit/sdk": "~5.0.0",    
+    "@fitbit/sdk": "~4.2.0",
...
 "buildTargets": [
-      "atlas",
-      "vulcan",
+      "mira"
    ],
```

According to [this forum user](https://community.fitbit.com/t5/SDK-Development/Fitbit-Versa-2-development-issue/m-p/5385315/highlight/true#M19325) we also need to change some filenames in the scaffolded project. We must rename `index.view` to `index.gui`, `widget.defs` to `widgets.gui` (note the plural change), and edit the contents of `widgets.gui` to point to `/mnt/sysassets/widgets_common.gui` instead of the file it points to.

Also, lol, the highest supported version of node is 16, so make sure you're using node 16 or lower, preferably with something like `nvm` so you can go back to the present day easily. (Poor Fitbit!)

Once you've done all that, you _should_ be able to start the fitbit CLI with `npx fitbit`, then `build` and (assuming the Fitbit simulator is up and running Mira) `install`.

![Boom.](/assets/fitbit-hello-world.png)

Huh. Aren't clocks supposed to, uh, tell time?

Follow the [Fitbit getting started tutorial](https://dev.fitbit.com/getting-started/) to turn this blank screen into a clock. TLDR: Edit `resources/index.gui` (remember we renamed this from the `.view` file used in later SDK versions), `styles.css`, and `app/index.js` with the provided code, run `build` and `install` (or `bi` which apparently is shorthand for both) and you get a very nice clock:

![picture of a not-actually-very-nice clock face on the fitbit simulator](/assets/fitbit-clock.png)

Okay, it's... fine. But hey, it's up and running. Now let's do something cooler with it... in a future post.

