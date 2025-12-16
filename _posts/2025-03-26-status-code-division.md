---
layout: post
title: "What I Learned at Work Today: Status Code Tricks"
categories: things-i-learned
tags: java math
excerpt_separator: <!--more-->
description: Math is even harder if you're a computer.
---

At work yesterday, I came across this snippet of code in a Java class meant to handle HTTP responses:

```java
boolean isSuccessful(int statusCode){
    return statusCode / 100 == 2;
}
```

My first instinct was to chuckle (and in fact I sent it to a coworker and we both chuckled). What a silly way to test if something equals 200! I figured whoever wrote this years ago was just having a clever laugh at future coders' expense.

Then today I sent it to another coworker, who pointed out my error, which is that most (all?) typed languages handle integer division by returning an integer.

In Javascript you can just do:

```js
console.log(3/2);
```

and you'll see `1.5` displayed on the screen. This is how humans do division, and it's still how I instinctively think about numbers. But in Java (and Python2, and C, and plenty of other languages), dividing an int by an int produces another int. (This is not intuitive for a lot of people, as evidenced by the cornucopia of posts on sites like [Stackoverflow](https://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-division-keeps-rounding-down-to-0).) That means in the snippet above, `statusCode / 100 == 2` would return true for a 200, but also a 204, a 202, or any other 2xx code.

Pretty smart!
