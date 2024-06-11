---
layout: post
title: "More Fitbit Dev Resources"
categories: things-i-learned
excerpt_separator: <!--more-->
---
![a stock photo of a person wearing a smartwatch. I'm not even sure if this is an actual fitbit.](/assets/is-this-even-a-fitbit.jpg)

The developing-for-fitbit journey continues...

### Breaking changes between SDK 4.x and 5.x

The older Fitbit I have, a Fitbit Versa 2, uses software written with version 4.x (or lower?) of the Fitbit SDK. Modern Fitbits use... I think it's up to 6.x? And excitingly, there were a ton of breaking changes between version 4.x and 5.x.

I solved a number of the issues [here](/things-i-learned/2024/05/24/fitbit-dev.html), but am running into more, especially with premade Fitbit components like buttons--which, incidentally, are very poorly documented.

However! Pure luck and a lot of random web searching led me to this official Fitbit demo project: [https://github.com/Fitbit/sdk-exercise/](https://github.com/Fitbit/sdk-exercise/). And we're in luck, the initial version was written with SDK 3.0 and then was abandoned shortly after, even though all of Fitbit's developer docs were updated for 5.0 when the Versa 3 came out. In other words, it's an ideal resource for learning how things 'used to' be done.

From that I found that if I want to place a button on the screen on the Versa 3, I would import `<link rel="import" href="/mnt/sysassets/widgets/text_button.defs" />`, but if I want to place a button on the screen on the Versa 2, I should import `<link rel="import" href="/mnt/sysassets/widgets/square_button_widget.gui" />`. 

I'm not even a hundred percent sure how to browse that widgets directory, if it's even possible; I suspect it's built into Fitbit's firmware and can't be accessed by humans. Which makes this dead repo possibly the best source of truth for SDK 4.0 widget names?

There are a number of other demo projects in various states of completion in the [Fitbit github organization](https://github.com/orgs/Fitbit/repositories?type=all). I believe the repos beginning with `sdk-` are the most useful, but take a look.

### General help

Bless [this Aussie developer](https://gondwanasoftware.au/fitbit/sdk-faq) who has 1) made about a thousand watchfaces for Fitbit (including not one, but two watchfaces that [actually play Pong](https://gondwanasoftware.au/fitbit/products/stench)) and 2) written up his own [SDK guide](https://gondwanasoftware.au/fitbit/sdk-faq) filled with helpful tips.

Hopefully these resources help you as they are helping me. And I hope I will have an update on my own app(s) soon!
