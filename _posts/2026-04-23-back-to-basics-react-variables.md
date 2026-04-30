---
layout: post
title: 3 ways to store variables in React, and why you shouldn't sleep on useRef
categories: things-i-learned
excerpt_separator: <!--more-->
description: "(or: useRef isn't only for DOM manipulation)"
---

React's `useRef` hook is a really powerful tool. I mostly use it as a way to 'break out' of React and interact directly with DOM elements. My sister and I used `useRef` heavily with (Noodle) in order to implement accessibility features like auto-focusing on alert banners. I used `useRef` in a project last year (that I've been too busy to write up) that let me write data directly to an HTML Canvas within a larger React app.

But [React's own docs](https://react.dev/reference/react/useRef) list DOM manipulation as the secondary use case (although a "particularly common") one. The primary use case, according to the docs, is keeping track of information that you want to access, potentially change, and persist between renders.

But what does this mean, exactly?

A web search for "react const vs state vs ref" turns up dozens of results, so that makes me think that this is a topic of some confusion for folks other than myself, so why not add my version to the pile?

I've made three very simple codePen examples to demonstrate the three ways to store variables in React, so buckle up and follow along.

## Option 1: vanilla JS variables

<script async src="https://public.codepenassets.com/embed/index.js"></script>

{% include codepen.html slug="NPRBgRq" title="local vars" %}

Data stored in a vanilla JS variable can be modified but will not persist across re-renders.

It also won't cause a rerender if it is changed.

Click the button to increase the counter. Nothing happens in the UI. If you check your console, you'll see that the count is increasing, but because React's internal reconciliation isn't running, the UI doesn't update. If you force a rerender by updating a different prop (here, the creatively named `thing`), the value resets to its initial value.

Does this mean we don't use vanilla variables in React? Of course not - they're a perfect "scratch pad" for temporary calculations.

## Option 2: storing in state

{% include codepen.html slug="VYKBWvG" title="State" %}

Ah, the classic. This is the one everyone knows. Data stored in state represents something that persists across re-renders, can change over time, and is important for the component to render. Change the state, change the UI. Click the button to see the clicked counter increment. If you re-render this component, it will (usually) preserve state (exceptions are detailed in [this doc](https://react.dev/learn/preserving-and-resetting-state)).

## The third way: storing in a ref

{% include codepen.html slug="PwGBjjY" title="Ref" %}

This is the option that I haven't used much until recently. By storing a variable in a ref, you're saying that you want the data to be changeable and persist across renders, but NOT affect the UI.

Notice how when you click the button to increase the counter, it increases, but the UI does not change. But if you force a re-render by updating a different prop, the UI updates (and does not reset the value).

This makes useRef fairly useless for storing values that should affect the UI, but excellent for storing other types of data. Judging by the number of Medium posts on this topic, a common use case is timers, although I've never used useRef this way.

Recently, I used it to store data streaming from a backend until I was ready to trigger a rerender, since the stream was not necessarily in sync with the UI actions I wanted to take.

Basically, any time you want data to persist across renders but not affect the UI, useRef is the way to go.

This is a pretty specific use case. For example, I have trouble thinking about how I'd use this at work, where our UIs are fairly straightforward. But I'm still glad to have this in my toolbox.

### Resources

- [Preserving and resetting state](https://react.dev/learn/preserving-and-resetting-state)
- [When to use refs](https://react.dev/learn/referencing-values-with-refs#when-to-use-refs)
