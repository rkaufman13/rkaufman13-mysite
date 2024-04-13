---
layout: post
title: "Typescript-ifying Noodle"
categories: things-i-learned
excerpt_separator: <!--more-->
---

![Javascript is great because it lets you do anything](/assets/javascript-is-fun.jpeg)

Over the spring and summer, I built [Noodle](https://noodleapp.cool), a minimalist, privacy-focused event scheduling app. ([more](./noodle-app)) My friends and I use it all the time, but development has kinda slowed.

This is a problem, because if I ever need to fix anything, I'm going to have to go back and remember how the code works, from scratch.

Javascript is _so_ permissive. It's great that I can get up and running without having to worry about whether I'm comparing a string to an int, but future me is going to step on that rake, I know it.

Separately from the conversation I'm having with myself about how to ensure code maintainability without having to remember why I made all the decisions I did, my mentor at work suggested converting the project to Typescript. So that's two people telling me to do this, so here we are.

<!--more-->

We use TS at work, but I'd never started with a JS project and had to convert it mid-stream. The resources I have found that have helped are:

- [Typescript's official page on migrating to TS](https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html)
- [React's docs on adding TS to an existing project built with create-react-app](https://create-react-app.dev/docs/adding-typescript/)  The docs are a bit out of date for TS 5+; you'll also need to add this to your package.json:

```json
 "overrides": {
    "typescript": "^5.0.3"
  }
```

- [React Typescript cheatsheet](https://react-typescript-cheatsheet.netlify.app/docs/basic/getting-started/function_components/)

Once I added TS to the project, I could start renaming files. My IDE started complaining about all sorts of things. Javascript really lets you get away with anything.

Full disclosure, I have only started to tackle the very 'easy' components, so Noodle is not fully Typescript-ified yet, but I'm looking forward to the day I can say that it is.