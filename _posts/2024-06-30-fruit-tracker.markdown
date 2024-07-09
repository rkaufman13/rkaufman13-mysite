---
layout: post
title: "Fruit Tracker, my first Fitbit app, is live"
categories: stuff-i-made
excerpt_separator: <!--more-->
project: "Fruit Tracker"
---

![Image of a beautiful apple in the grass](assets/apple.jpg)

[My first Fitbit app](/fruit-tracker.html) is live in the [Fitbit app store](https://gallery.fitbit.com/details/74375fbf-752f-4ead-8d08-72293e63082a).

You can read about what it does [here](/fruit-tracker.html). Below are some things I learned while making it.

- **The fitbit onboard computer is very stupid.** This is probably why Fitbits have such good battery life. You can do very basic calculations on the Fitbit itself, and render or unrender components, but if you want to do anything else like:
  - Connect to the internet/fetch data from an API
  - Store a variable to be retrieved next time the app is opened
  - Download images
  - Get a GPS heading
  - Do anything while the watch is off/idle

  You need what is called a "companion app," another Node app that runs on your phone, rather than on the watch itself. (I suspect that making the watch super dumb is partly why its battery life is so good.) The heavy compute functions are offloaded to the phone and you simply pass data back and forth from the phone to the watch using the built-in [Messaging API](https://dev.fitbit.com/build/guides/communications/messaging/), or a different File Transfer API if you need to move large files. (Messaging API is limited to 1KB of data per message, which was not a problem for Fruit Tracker, but has caused me to have to get creative with another app I'm working on.)

- By the way, the companion app and watch app can only send strings, so get comfortable with JSON.stringify() and JSON.parse().

- **Manual positioning of elements is for suckers.** You can totally declare an svg element and position it like:

     ```html
      <text fill="white" x="50" y="15" text-anchor="middle" font-size="20" id="yesterday">
     ```

     And in fact I have done that with a number of components, but the winning way is to use Fitbit components. (I mentioned those components in a [previous post]({% post_url 2024-06-05-fitbit-sdk-version-differences %}).) Those come prestyled, they are easy to place, and using them also ensures that you're consistent with the rest of the watch UI.
  
  Finally, the last thing I learned from building Fruit Tracker is....

- Eating the 'right' amount of fruits and vegetables is freakin' hard. I thought I was doing well until I started actually tracking my consumption. Good news is, I have almost immediately increased my fruit and vegetable intake by at least 50%. I can't imagine a better example of using measurement tools to make change.
