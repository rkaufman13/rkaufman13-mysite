---
layout: post
title: "TIL: Cleaner Log Output When Using 'Concurrently'"
categories: things-i-learned
excerpt_separator: <!--more-->
description: I knew there had to be a way to make its output more readable.
image: /assets/concurrently.jpg
---

![People's legs and feet on a racetrack. They're about to begin running at the same time.](/assets/concurrently.jpg)

If you've ever used the package [`concurrently`](https://www.npmjs.com/package/concurrently) to run more than one thing at the same time while developing, you probably have seen how the logs are a little jumbled together. All output is logged to the console, by default, with a number representing the process that created the output. As an example, here's a Vite frontend and a toy websocket server in the backend that logs every message received from the FE:

```bash
[0]   VITE v7.3.0  ready in 220 ms
[0] 
[0]   ➜  Local:   http://localhost:5174/
[0]   ➜  Network: use --host to expose
[1] received: { 'message': 'hi' }
```

This is...fine? But it's easy to miss the [0] or [1], it's just one number and honestly if you're not looking for it it just sort of fades into the background.

But by passing the `--names` flag in you can call your processes anything you want.

`concurrently --names frontend,backend 'vite' 'node src/server.js'` turns the above output into:

```bash
[frontend]   VITE v7.3.0  ready in 220 ms
[frontend] 
[frontend]   ➜  Local:   http://localhost:5174/
[frontend]   ➜  Network: use --host to expose
[backend] received: { 'message': 'hi' }
```

And of course you can use more descriptive names, although these are plenty for me.

I wasn't able to find the official documentation on this, although there is [documentation on how to interact programmatically with concurrently](https://www.npmjs.com/package/concurrently#api) and pass in the names options. I'm not sure how to incorporate that into a development pipeline but that's a me problem. For now, the command-line flag is all I need.
