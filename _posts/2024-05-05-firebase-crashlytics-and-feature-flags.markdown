---
layout: post
title: "Firebase Crashlytics and Feature Flagging, or What I Learned at WITS Spring 2024"
categories: things-i-learned
excerpt_separator: <!--more-->
---

_The following info comes from the [Women in Tech Summit](https://womenintechsummit.net/spring-2024-summit/) which I attended in Philadelphia this weekend. I may type up a more fluffy post about how it felt to attend this conference later, but for now, these are my technical notes from the hands-on session I attended._

Android app development seems a lot more complex than web-app development. I might be wrong, I've built a lot of web apps but no Android apps. (Yet; I just got a Fitbit Versa and feel like that postage-stamp-sized screen is crying out for me to do something with. Apparently it [doesn't run DOOM yet...](https://www.reddit.com/r/fitbit/comments/b80035/made_some_progress_with_porting_doom_to_fitbit_os/))

Anyway, making an app run on the hugely fragmented Android ecosystem, as well as keeping users' versions up to date (including forcing them to update if there's a critical security fix) seems like a huge problem. Presumably there are enterprise solutions for this but in my hypothetical DOOM-on-Fitbit scenario where it's just me, what's the solution?

Google Firebase has some great options for solving these problems, which I learned about from two Comcast engineers. [Crashlytics](https://firebase.google.com/docs/crashlytics) can help track and centralize crash data from multiple devices, and [Remote Config](https://firebase.google.com/docs/remote-config) can manage some app features without having to publish a new version of the app.

<!--more-->

## Crashlytics

In this workshop, we started from the beginning, so that's how this blog post will start. Download [Android Studio](https://developer.android.com/studio) if you don't already have it and run through the setup process to create a new project. This defaulted to Kotlin for me, but you can also use Java.

<img src="/assets/firebase_app/first_app.png" alt="boilerplate Kotlin app" class="post"/>

Now, connect Android Studio to your Google account, for the Firebase features you want to use. If you are logged into the Google account you want to use with Firebase, this is nearly a one-button process. Click Tools->Firebase->Crashlytics and then Get Started. Click the button to integrate your Firebase account with Android Studio.

I had some issues with my default browser defaulting to my work Google account, while I wanted to use my personal Google account for this project. Long story, but you can also connect your project to Firebase manually. Go to [Firebase Console](https://console.firebase.google.com/) and create a new project:

<img src="/assets/firebase_app/first_firebase.png" alt="creating a new firebase project" class="post"/>

I skipped adding Analytics.

Add Android to your project:

<img src="/assets/firebase_app/add_package.png" alt="screenshot of adding the package to your app" class="post"/>

The package name must match the package name of your app.

Google will then provide you a json file with the configuration required to connect the app to your Firebase resources. It even tells you where to put it:

![Google instructions for downloading and installing the configuration JSON](/assets/firebase_app/google_instructions.png)

Back in Android Studio, add the Firebase Crashlytics SDK to your dependencies and reload the project.

Now Crashlytics is monitoring your app for crashes, across all devices it's installed on. To test it, we can also follow the instructions provided in Android Studio's setup--force an error.

Edit the boilerplate Greeting function to look like this:

```
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Column(modifier = Modifier.fillMaxSize(), verticalArrangement = Arrangement.Center, horizontalAlignment = Alignment.CenterHorizontally) {
        Text(text = "hello i am an android app")

        Button(onClick = { throw RuntimeException("An error occurred")}) {
            Text(text = "Click to crash the app")

        }
    }
}
```

Here is that app running in the simulator:

<img src="/assets/firebase_app/pretty_button2.png" alt="very good app" class="post"/>

I am not an expert at app design, clearly. :)

Now, when you click the button, the app will crash and you'll see the stack trace in Firebase.

![I used slightly different wording in the workshop as you can see](/assets/firebase_app/you_done_goofed.png)

I can see how useful this would be for monitoring errors on apps installed on multiple types of phones, running multiple versions of Android! I kinda wish Crashlytics worked with web apps too - but it appears to only support apps.

## Remote Config

After we hooked up and tested Crashlytics, we experimented with [Remote Config](https://firebase.google.com/docs/remote-config). This is essentially a feature flagging tool, so you can have more control about rolling out or rolling back features, do A/B tests, geographical rollouts, and more.

The steps to set up Remote Config are the same as above: connect your app to Firebase (if you haven't already) and add the Remote Config SDK to your project. Then we need to set up some variables as well as sensible defaults.

Let's say you're planning to roll out a new feature and you want to be able to hide the button to launch the new feature until it's ready. We can set a boolean showButton flag like so:

```
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier, showButton:Boolean) {
    Column(modifier = Modifier.fillMaxSize(), verticalArrangement = Arrangement.Center, horizontalAlignment = Alignment.CenterHorizontally) {
        Text(text = "hello i am an android app")
        if (showButton) {
            Button(onClick = { /*launch my cool new feature*/ }) {
                Text(text = "Click to launch the cool feature")
            }
        }
    }
}
```

So how do we decide what the value of `showButton` is? In our main activity, in the `onCreate` function, let's fetch our values from Remote Config.

```
val remoteConfig = Firebase.remoteConfig
val configSettings = remoteConfigSettings {
            minimumFetchIntervalInSeconds = 3 //in a production app this should be much higher
        }
remoteConfig.setConfigSettingsAsync(configSettings)
```

These lines tell your app to connect to Firebase, find any remote config values you've set, and set them in the app.

We also need to set a default in case the user is not connected to the internet, or if Firebase is down.

```
remoteConfig.setDefaultsAsync(R.xml.remote_config_defaults)
```

What does that file look like? It's in your `res/xml` file and it's an XML doc of key-value pairs:

```
<?xml version="1.0" encoding="utf-8"?>
<defaultsMap>
    <entry>
        <key>buttonText</key>
        <value>Click</value>
    </entry>
    <entry>
        <key>showButton</key>
        <value>false</value>
    </entry>
</defaultsMap>
```

(As you can see, I was also working on using a flag to set the button text. If you just need the boolean, you just need the boolean.)

Now we have instructions for fetching the remote config file, as well as populating the fields with defaults if needed. But we still need to assign each value to a variable within Kotlin. Our Comcast instructors suggested the following pattern. I suspect there is a simpler way, however, this will work. Within your setContent function:

```
var showButton by remember { mutableStateOf(remoteConfig.getBoolean("showButton")) }
remoteConfig.fetchAndActivate()
                .addOnCompleteListener(this) { task ->
                    if (task.isSuccessful) {
                        val updated = task.result
                        Log.d(TAG, "Config params updated: $updated")
                        showButton = remoteConfig.getBoolean("showButton")
                        Toast.makeText(this, "Updated to latest version",
                            Toast.LENGTH_SHORT).show()
                    } else {
                        Toast.makeText(this, "An error occurred",
                            Toast.LENGTH_SHORT).show()
                    }

                }

remoteConfig.addOnConfigUpdateListener(object : ConfigUpdateListener {
                override fun onUpdate(configUpdate : ConfigUpdate) {
                    Log.d(TAG, "Updated keys: " + configUpdate.updatedKeys);

                    if (configUpdate.updatedKeys.contains("showButton")){
                        remoteConfig.activate().addOnCompleteListener {
                            showButton = remoteConfig.getBoolean("showButton")
                        }
                    }
                }
```

Obviously the toasts are optional as are the logs; this still feels like a lot of boilerplate code, but it ensures that your values update automatically as soon as they're changed in Firebase console.

We need to pass the `showButton` parameter into our function:

```
  Greeting(
            name = "Android",
            modifier = Modifier.padding(innerPadding),
            showButton
        )
```

All that's left to do is create the parameter in Firebase.
![create the parameter in firebase](/assets/firebase_app/show_button.png)

Now every time you update the parameter within Firebase (don't forget to hit Publish after saving your changes) your app's behavior will change almost instantly. No code deploy needed.

![side by side view](/assets/firebase_app/side_by_side.png)

Neat, right?

In addition to booleans, you can store text strings, numbers, and JSON. And Remote Config does work with not just app apps but also web apps. I can imagine a number of applications for this tool, ranging from the useful (gating new content behind a feature flag) to the silly (changing a greeting message on the fly).

In all this was a super useful workshop and I'm looking forward to integrating these features into my next project.
