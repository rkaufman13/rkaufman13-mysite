---
layout: post
title: "Local Firebase, or, how I learned to stop trashing my prod db"
categories: things-i-learned
excerpt_separator: <!--more-->
project: "Noodle"
---

[Noodle](https://noodleapp.cool) has a lot of the hallmarks of a solo dev side project, which is fair, because it is. Stupid simple deploy pipeline (which is probably a good thing), no tests to speak of (probably not a good thing), no real dev environment. That means when I test Noodle locally I hook up to the prod Firebase db, and usually end up writing a lot of bogus data to it along the lines of:

- "test event"
- "test event 2"
- "asfdkf;;; why wont you work"

and so on. This isn't really a problem, as Firebase lets me have a GB of data before I have to start paying them -- that is a lot of JSON -- but it's kinda messy. And now that I'm converting Noodle to Typescript, I'm doing a _lot_ of testing.

Enter the [Firebase Emulator Suite](https://firebase.google.com/docs/emulator-suite/connect_and_prototype). I got it set up so I can run a local copy of my database on my machine and not worry about junk data polluting the real database.

Here's how I did it.

<!--more-->

Step 1: [Install the Firebase CLI tools](https://firebase.google.com/docs/cli). On a Mac, you can either do this with `npm install -g firebase-tools`, if you want NPM to manage the tools, or run this script provided by Google:
`curl -sL https://firebase.tools | bash`

Follow the rest of the steps on the page to authenticate and test the connection.

Step 2: Initialize the root directory of Noodle as a Firebase project with `firebase init`. The init script will ask a few questions about your project as well as what Firebase tools you want to enable.

One very cool and unexpected perk is that it copies your database rules (which I laboriously created in the console over many cups of coffee and some cursing) to a local file which, presumably, can then be synced back up to the prod DB. Or at least cut and pasted.

Step 3: Run `firebase emulators:start` to see your database at localhost:4000.

Step 4: Install Java (:

![Why would I have Java installed on my ancient personal Macbook](/assets/java-error-message.png)

Step 5: Run `firebase emulators:start` to see your database at localhost:4000.

Step 6: Add code branching in your app to use the correct db when developing.

```javascript
if (process.env.NODE_ENV === "development") {
  connectDatabaseEmulator(app, "localhost", 9000);
}
```

Don't make the mistake I did of thinking you can just set your database URL in your db config. Firebase does not like that.

A thing I didn't know: If you used `create-react-app` to create your React app, then your `start` and `build` scripts automatically set the appropriate NODE_ENV value for you.

That's basically it - you're now writing to a dev db that cleans itself out on restart. All in all this was a project that intimidated me but only took about an hour to set up, and I'm glad I did.
