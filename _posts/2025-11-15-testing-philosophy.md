---
layout: post
title: My 4 Testing Commandments
categories: opinions
tags: unit-tests
excerpt_separator: <!--more-->
description: Four things I believe about tests.
image: /assets/bug-hunting.jpg
---

![An image of a beetle (not technically a "bug") under a magnifying glass](/assets/bug-hunting.jpg)
*Bug hunting*

This week I was a guest instructor at the [Black Venture Capital Consortium's Software Engineering Career Track](https://www.bvcc.vc/hbcu-curriculum). This is was my second year volunteering with BVCC on the SWE track, and it's super rewarding, although I'm still learning how to deal with the "Gen Z stare" on Zoom. (Teachers who do a lot of online instruction, my hearts go out to you.)

This year, my topic was testing -- both manual and automated. The students are pretty new to software engineering, so manual tests were more their speed, for the most part, and we had fun trying to break a demo application.

But automated tests are the thing software developers will spend more of their time on than manual, so I tried to give them a little taste of automated testing principles.

This is, more or less, what I said:

**Tests are your contract**. When you write tests, you're forced to decide how a method *should* behave. This is where you can decide that a method will throw an error when given bad data vs printing a message in the console. This is where you decide that no, you're not going to allow this edge case. Tests help you think through what you want to code, and six months later, they help you remember what you meant to code.

**Always test your tests.** You can use a [mutation testing framework](https://blog.nashtechglobal.com/mutation-testing-dont-let-your-code-get-wrecked-%f0%9f%92%80/) or just manually, temporarily, modify your code or test assertions. (Sometimes I just change all `assertTrue`s to `assertFalse`s.) But without knowing that your tests are doing what you think they're doing, you can't have confidence in them.

**Don't put too much stock in unit test examples when you're learning.** Many, many "how to write unit tests" blog posts use math as their example. This makes sense, because if you know that 2+2=4, it's easier to focus on the syntax of the test code, and you don't need to waste brainpower on understanding what the method-under-test is doing. But if you're new to unit testing, you might be asking yourself, "why on earth would I need to test that 2+2=4"? You don't. You'll *never* write a unit test testing an "add" method in production, because you will never write an "add" method. Don't focus on the method-under-test, just pay attention to the syntax and trust that it gets more interesting.

**Tests and accessibility go hand in hand**. Okay, this is more about integration tests for a web app than unit tests, but most good testing libraries, such as React Testing Library, use the same affordances to run tests on rendered elements as a screen reader user would use to interact with a page. If it's hard to test, it's probably hard for a screen-reader user to use. (I don't feel confident saying that if it's easy to test, the site is accessible--but it can't hurt.)

What would you add to these four?
