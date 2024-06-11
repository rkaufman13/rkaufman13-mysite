---
layout: post
title: "Common Errors When Developing for Fitbit"
categories: things-i-learned
excerpt_separator: <!--more-->
---

Or maybe just common to me?

![Image of the Fitbit developer bridge on a watch](/assets/fitbit-developer.png)

**Problem:**

```Install failed: RPC call to 'app.install.stream.begin' could not be completed as the RPC stream is closed```

**Cause:**

Jury's out on what causes this. It seems to happen when I sleep my laptop; the Fitbit simulator doesn't seem to be able to recover.

**Solution:**

Remove `~/Library/Application\ Support/Fitbit\ OS\ Simulator/`, which contains caches, preferences, etc. You'll have to reset your preferences afterwards of course.

<!--more-->
---

**Problem:**

```Error 22 Critical Glue Error```

**Cause:**

Unsupported SVG code in `index.gui`. It appears that Fitbit OS only supports a subset of W3C-compliant SVG tags and attributes.

**Solution:**

Only use the tags and attributes supported [here](https://dev.fitbit.com/build/guides/user-interface/svg/).

---

**Problem:**

```No phones are connected and available```

**Cause:**

I got this one when trying to stop using the Fitbit simulator and instead sideload my app-in-development to my watch. To load an app onto your watch, you need to both connect the watch and your phone to the CLI developer bridge.

On most (all?) Fitbit watches, you can connect your watch by going into Settings, scrolling to the bottom, and clicking "developer bridge." But how to connect the phone?

**Solution:**

Within the Fitbit app, click on the icon for your device, then scroll to Developer Menu, and connect to the Developer Bridge that way. I did not find this intuitive, by the way.

---

**Problem:**

```Failed to fetch - permission "access_internet" was not granted.```

**Cause:**

This is another fun one -- the simulator doesn't support 'permissions' which means, actually, that all permissions are allowed. On an Android phone, of course, you need to declare what permissions you need.

**Solution:**

Request permissions in your package.json like so:

```json
   "requestedPermissions": [
      "access_internet"
    ],
```
