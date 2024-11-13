---
layout: post
title: Webpack, Explained by Someone Who Just Learned What It Is
categories: things-i-learned
excerpt_separator: <!--more-->
description: I whiffed this question recently.
image: /assets/packing_boxes.png
---
![An illustration of shipping boxes being packed up.](/assets/packing_boxes.png)
*Image by [digital designer](https://pixabay.com/users/dapple-designers-7874104/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4399301) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=4399301)*

What is webpack?

At a recent casual meeting of Women & Gender eXpansive Coders DC (a local group I've become involved with over the past year) a Python user asked me this question, and boy did I stutter out a non-answer. I think I said something like, "Webpack is a build tool that magically bundles all your Javascript for the web."

Does that sentence actually mean anything? I mean, I think I got the basics down, but I did use the word "magically," so negative points for that. Also, pretty sure I inserted about a million "um"s as well.

I work with Javascript pretty much daily at work, but I've never really put much thought into Webpack or other Javascript build tools. That's probably a good thing -- after all, it _shouldn't_ be something I need to think about -- but I decided I should have a slightly deeper level of understanding of these tools that are ubiquitous in modern front-end development.

For this post I'll be talking about Webpack exclusively, but know that it's not the only tool out there.

## Okay, but what is Webpack, actually? ##

(Most) modern websites need Javascript to run. (This site uses no JS, thank you Jekyll.) Javascript used to be just added to the top of each page where you wanted to use it:

```html
<!--index.html-->
<html>
    <head>
        <script src="notavirus.js"></script>
    </head>
    <body>
    ...
    </body>
</html>
```

```js
//notavirus.js
window.alert("Your computer has been compromised!
Click here to download our malware remover!")
```

And that worked fine for years. It was all we had and we were okay with that.

<!--more-->

But then people started making reusable javascript snippets, which became whole packages that you could download. So maybe you now want to download `definitelynotavirus` and use it on your page. You could just download it, and stick it in your script tag, but if the maintainer of `definitelynotavirus` updates their code, you'd have to know to go get the latest version yourself.

So instead there sprung up package managers. Today, `npm` is probably the most well known one (followed quickly by `yarn`). There used to be one called `bower` that I've personally never used. `npm` will automatically download the latest version of `definitelynotavirus` and install it onto your computer. `npm` will know where on your computer the `definitelynotavirus` script lives (probably somewhere like `node_modules/definitelynotavirus/script.js`) and so when you type `var notavirus = require('definitelynotavirus')` it knows exactly how to find that script on your file system.

Wait a minute, file system?

So `node`, the Javascript runtime that can run outside of a browser, knows about `require` and paths on your file system. A web browser...does not. A web browser assumes that every HTML file that uses Javascript has a `<script>` tag at the top for every script you want to use.

And that is where bundlers like webpack come in.

When you run webpack, it essentially traverses your website, finds `require` statements and replaces them with code that a web browser can understand. Essentially, going back to that old `<script src=>` format.

While we're at it, why not have webpack minify your Javascript by removing comments, shortening variable names, and removing whitespace?

And if we throw in `babel` we can have access to modern Javascript features, such as template literals or spread syntax, without worrying that they also can't be understood by the web browsers reading them. (Web browsers are kinda dumb maybe?)

| *Note: `babel` is not a bundler, it is a `loader` (and the type of function it provides is called `transpiling`). Think of webpack as the orchestrator that both bundles all your content and also triggers the running of other operations. A `loader` works at the file level and makes changes to each file before it is put into the bundle; a `plugin` works on the finished bundle itself, but people seem to use all kinds of terms for this stuff.*

Also, let's say that `definitelynotavirus` contains tons of functions, but you only need one. Webpack is smart enough to extract only the functions you have imported. It is even smart enough to create multiple bundles and load only what you need, when you need it.

Modern Javascript usually uses some sort of task runner to kick off all these tools, these days `npm` or `yarn` can do that for you with [custom scripts](https://docs.npmjs.com/cli/v10/using-npm/scripts). For example, if you create a new React app with `npx create-react-app`, `npm run build` will be automatically defined for you as `react-scripts build`.

That script is found inside `your_project/node_modules/react-scripts/scripts/build.js`. It does a bunch of React-specific/not-React-specific-but-opinionated things, and then...

```js
  const compiler = webpack(config);
  return new Promise((resolve, reject) => {
    compiler.run((err, stats) => {
    //goes on for multiple lines
     });
  });
```

So this is how React kicks off webpack for us - by calling it within `build.js`, which is created automatically for you when you create a new React app.

Big companies most likely have their own tooling path (I know we do at work) but somewhere in there, you're likely invoking webpack.

### Resources ###

- Serious props to [Modern Javascript Explained for Dinosaurs](https://medium.com/the-node-js-collection/modern-javascript-explained-for-dinosaurs-f695e9747b70) which I borrowed heavily from to make this post.
- An [older guide to using Webpack](https://github.com/petehunt/webpack-howto), designed for readers familiar with Browserify, Webpack's predecessor
- [Understanding the Modern Web Stack](https://dev.to/alexeagleson/understanding-the-modern-web-stack-webpack-part-1-2mn1#why-bundling)
- [Webpack, the confusing parts](https://rajaraodv.medium.com/webpack-the-confusing-parts-58712f8fcad9)

### Note ###

Thanks to my coworker who reviewed this post for accuracy. Any mistakes that remain are mine :)