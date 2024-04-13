---
layout: page
title: "Noodle"
date: 2023-10-24 12:16:11 -0500
categories: projects
permalink: "noodle-app"
hero: "noodleapp.png"
built: June-September 2023
---

![the homepage of "Noodle"](./assets/noodleapp.png)

There once was a free webapp that allowed you and your friends to collaboratively decide on the best date to hang out — for a dinner party, game night, or whatever. Then that app added a few ads. And a few more. And then required all users to log in to use it, and provide an email address to receive email. And then moved a bunch of its best features behind a paid paywall. While I don't begrudge the makers of that app the need to make money (okay, maybe I do a little), I missed the app back when it was good.

Enter Noodle, which, if its name bears any resemblance to That Other App, is totally a coincidence.

Users can create an event (without creating an account), manage the event, send the event link to their friends to respond, close the event, and delete the event, all without seeing any ads or having to manage passwords.

I built it using Firebase, React, and a tiny bit of node/express for the backend server methods/to have a safe place to store my Sendgrid API keys. My husband helped configure the nginx server it runs on and my sister helped make it more accessible for people using screen readers. The app is free to use for everyone.

[Check it out!](https://noodleapp.cool)
