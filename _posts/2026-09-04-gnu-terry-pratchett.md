---
layout: post
title: "GNU Terry Pratchett - 'A man is not dead while his name is still spoken.'"
categories: things-i-learned housekeeping
excerpt_separator: <!--more-->
description: Fun with HTTP headers.
---

In "Going Postal", Terry Pratchett's 33rd book in the *Discworld* series, much of the plot revolves around "the Clacks," a communication network somewhere between the internet and a telegraph system. When John Dearheart, the son of its inventor, is murdered, a message is created to run up and down the Clacks forever: "GNU John Dearheart" - because, as the book says, "A man is not dead while his name is not spoken." The GNU is a bit of Clacks-ese that's supposed to signal to the Clack operators to pass the message on indefinitely. (Also maybe a joke about the GNU operating system, since "GNU's Not Unix" is a perfect bit of recursion? I don't know enough about Sir Terry to know if he was *that* kind of nerd, but he did use [six monitors](https://www.tumblr.com/noirandchocolate/637331670751756288/terry-was-once-asked-why-he-worked-across-six) so I would not be surprised.)

Well, over the last decade, nearly 2000 websites have added the HTTP header `x-clacks-overhead: GNU Terry Pratchett` , meaning that his name continues to travel the Internet and will never be forgotten. As of this week, this site is one of them.

With ngnix, it was pretty easy to add a custom header; if you manage your own server of any type, there are instructions [here](http://www.gnuterrypratchett.com/) to add your own. If you don't manage a server, but your site is behind Cloudflare, you should be able to [add a custom header at the Cloudflare layer](https://developers.cloudflare.com/pages/how-to/add-custom-http-headers/), although I haven't personally tried this.

And if you just want to know when someone has added the header, there is a [Chrome extension](https://chromewebstore.google.com/detail/clacks-overhead-gnu-terry/lnndfmobdoobjfcalkmfojmanbeoegab?hl=en) and one for [Firefox](https://addons.mozilla.org/en-GB/firefox/addon/x-clacks-overhead/).


As an aside, *Going Postal* is the only Discworld book I have in hard copy...and it's signed. (Thanks, Dad!)
