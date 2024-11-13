---
layout: post
title: "Getting Unblocked, Faster: 5 Lessons from Journalism (and One Bonus Lesson) That Can Help You Ask Better Questions"
categories: soft-skills
excerpt_separator: <!--more-->
description: My former career has taught me how to ask questions. Here, I'd like to share those tips with you.
image: /assets/questions.jpg
---

![A paper-collage style image of a bunch of question marks.](/assets/questions.jpg)

Most loyal readers of this site know that before I was a software engineer, I was a journalist. I pivoted to my new career during the pandemic and have zero regrets! But there are certainly times I am grateful for my journalism training.

Frequently those times are when I need to get unblocked. I believe I can get unblocked faster than the average person at my level because my former career has taught me **how to ask questions**. Here, I'd like to share those tips so that you, too, can ask better questions.

## 1. Find your expert, and embrace the directed question ##

If you're writing about the pandemic, you need Anthony Fauci on the line. If you're debugging React, who's your subject-matter expert?

At work, I try to notice who's really good at certain tasks, whether or not they're the official on-call for that task or service. I don't hit them up all the time, but if a question in a public channel goes un-answered, or something is extra-urgent, I'll send a quick DM.

Outside of work, I try to do the same, although sparingly. This blog is made using Jekyll, and for the most part I don't have to know any Ruby to maintain it, but you absolutely bet I took notes when a woman in my local women-in-tech meetup was solving leetcode problems with Ruby one-liners.

Where else to find your expert? If your company has a formal mentorship program, get matched up with a mentor, and find out what they're great at. Then say, for example: "I know we meet [biweekly, or whatever the time period is], but I'm new to [thing], and I know that's one of your strengths. Would it be OK if I reached out outside of our set meeting times if I have a question about [thing]?"
  
Are you part of a tech meetup, Discord, user group (are those still a thing)? Sometimes a *polite*, respectful note to a helpful person there goes a long way.

All this does not overrule the idea that public conversations are, in general, better than private ones, because if your conversation is public, more people can learn from the discussion. But realistically, sometimes you just gotta get an answer.

<!--more-->
## 2. Get the details ##

Journalists are taught "always get the name of the dog." That means that small details matter. When asking your tech questions, you don't have to go into enough detail that everyone knows your pet's name, but you should include enough detail that it's easy to help you out.

See these examples:

| My code doesn't work."

| "When I run my code, I get [specific error message]. I think it's coming from this line...

| "I'm having trouble getting my local dev environment to start up. Here's the error message I'm getting: ..."

| "When I deployed to dev, I got a success message from the API, but I didn't see my update in the database. Then I tried ... Here's the line I added: ..."

| "I'm working on a PR to add that functionality, but some of the older tests in the service are either flaky or broke due to my changes. I'm not sure why changes in the XYZ class would affect tests for the ABC class. Are you aware of them being coupled?"

Can you tell which question is easiest to answer? It's not a trick question, it's pretty obvious -- but you'd be surprised how many people ask questions like the first one. (Which, as you'll note, is more of a comment than a question...)

## 3. Embrace sounding dumb ##

It is tempting to ask a question that "proves" that you know all about the system you're working with, you just need help with oooone tiny thing...

Often that ends up making you look more foolish, as a core assumption you had might be wrong, or you provide too much context, or miss the point. It's equally tempting to not ask at all. Who wants to ask a "dumb" question, anyway?

The best part of journalism was when I'd get an email on Monday saying, "Can you write a story about this new black hole discovery by Wednesday?" That means having to learn enough about black holes in a few hours to interview a black-hole expert or two by the following day. It would be lovely to not sound dumb, but realistically: *they have been studying black holes for years.* They have a Ph.D in black holes. My goal could not be to sound smart, because there is no way that I, a 20-something with a liberal arts degree, could sound smart next to literal Dr. Black Hole.

The less time you waste worrying about "looking dumb," the better.

It's the difference between:

| Why are we using the HDFS database for this project?

and:

| Is HDFS a database?

(It's not.)

Or the difference between:

| Why can't I call [x internal endpoint]? I know it's supposed to update the y table.

and:

| I'm trying to call [x internal endpoint] which from the docs looks like it'll update a row in the [y database], but the example payload seems to be malformed, as I'm getting a 500 back.

## 4. Do your research ##

Even if you can't become an expert on black holes overnight, that doesn't mean it's a good idea to go in blind. Similarly, if you have a question on a new-to-you topic, you may not be able to become the world's foremost expert on that topic before you ask a question, but it's a great idea to try to get up to speed before asking.

Read the docs, try Googling the error message, search the Slack or Teams archive for other coworkers who have seen the same problem, experiment.

The times I have posted hastily (thinking, "I don't know how to solve this, and it's probably super complicated, so I should skip ahead to the part where I ask my coworkers for help"), I have often regretted it, as the answer is often within our Slack or internal docs. Don't skip the fundamental research. Even if you think you understand black holes, or Docker images, it's a good idea to check around before asking your question.

## 5. Get to the point ##

Despite what it may look like on TV, journalists usually don't have time to sit down with a guest for an hour-long interview. Make your time count. [Don't say hello](https://nohello.net/en/) on Slack. Respect folks' time and they'll be more likely to help out.

The [inverted pyramid](https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/the_inverted_pyramid.html) news structure is also important here. Most important information goes at the top, less important information comes later (in a later paragraph or within a thread).

## Bonus! Watch out for XY questions ##

There's no journalism tie-in here. I wanted one, but the concept of an XY question is endemic to software engineering -- I'm not sure other fields even know the term. But it's such an important tip that I couldn't let it pass.

An XY question is when you ask X, but you actually want to know Y. The classic example is someone asking [how to get the last 3 characters of a filename](https://xyproblem.info/#example-1) when what they really want to do is get its extension.

The way to not ask these questions is to make sure you are asking about your goal, not your process or perceived solution. If you need to ask about a solution, include other things you've tried and why you ruled them out. Provide as much context as possible (without writing a novel). If someone tries to help by asking "why are you trying to do that" or "what are you ultimately trying to accomplish" answer them!

## What's next ##

Next time you find yourself stuck on a coding problem, put these lessons from journalism to the test and see where it takes you!

### Resources/Other Opinions ###

* [How to ask good questions](https://jvns.ca/blog/good-questions/) (Julia Evans)
* [How I ask questions](https://navendu.me/posts/how-i-ask-questions/) (Navendu Pottekkat)
* [Asking questions the right way](https://vadimkravcenko.com/shorts/asking-right-questions/) (Vadim Kravcenko)
