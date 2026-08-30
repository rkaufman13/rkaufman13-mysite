---
layout: post
title: "User Testing on a Shoestring"
categories: opinions hacks presentations
excerpt_separator: <!--more-->
description: How to DIY your way to usability.
---

![A photo of a pair of shoes, untied.](/assets/2026/shoes.jpg)
*[Yasvanth Kumar, Pexels](https://www.pexels.com/@yasvanth-kumar-12469/)*

*This is a blog post version of the talk User Testing on a Shoestring, which I gave at [Tech Business Community 2026](https://www.hclbcommunities.com/conferences/tech-business-community-live-2026) as the keynote presentation. This is a topic I've been thinking about for literally years, and I was never able to get my thoughts together into a coherent whole until the Tech Business Community opportunity came along and forced me to. I'm grateful for the opportunity to do so and for these ideas to finally go out into the world.*

*If you're looking for the slides for this talk, they are [available online](https://rkaufman13.github.io/usertesting-on-a-shoestring/index.html).*

So you've made an app, a website, or some other product.

And then you release it.

And then... users discover it. That's good, right?

But maybe the users have Feedback. The buttons are the wrong color, fine. They don't like your concept of Uber for Pickleball for Dogs, fine. But what if their feedback is just..it's hard to use?
Or they don't give you feedback because they got frustrated and walked away first?

This is what happens. It's inevitable. Your perfect thing meets real-world users, and...flop.

One tool that can help with this is something called user testing.

I've led user testing (non-professionally), been a user tester (professionally), and encouraged other people to do user testing (non-professionally.) I want to talk about guerilla, DIY, hacky user testing from my perspective -- the perspective of a non-professional UXer -- so that you, also a non-professional UXer, can do it too.

## What is user testing?

The industry leaders, Nielsen Norman Group, define user testing this way:

>In a usability-testing session, a researcher (called a “facilitator” or a “moderator”) asks a participant to perform tasks, usually using one or more specific user interfaces. While the participant completes each task, the researcher observes the participant’s behavior and listens for feedback.

My lazy definition is:

> Putting your app in front of people because you can't learn how people use it unless you watch them

(replace "app" with "website," "product", whatever.)

In other words, user testing is a way to gain insight into how actual people are using your app, which is kind of the point, maybe?

This is hugely oversimplified, but the gist is, let's put our thing in front of people and watch them use it. We'll then use the data we get from watching them to make it better.

Does this sound fun? Or at least useful? Read on...

<!--more-->

To do basic user testing we need:

- some (minimal) tooling (seriously can be just your phone camera and some paper)
- a hypothesis or an idea we want to test
- some people to test

I'll talk about some free or cheap ways to get all these things.

This post is for you if you are NOT a UX professional. This is 101 level stuff. At best. You'll get the most out of this post if, like me, you've worked for tiny nonprofits, or volunteered your time where there is literally no money, or maybe you're a solo entrepreneur doing everything yourself.

But basically, if you work somewhere where there is a chain of command and possibly a budget for this stuff, maybe try asking for budget for a UX person (as a consultant if you're really not able to get FTE headcount) before you ask for budget to DIY some user tests. And if your boss says no, then go ahead and DIY.

## Why do I have anything useful to say about user testing if I'm not a UX pro?

I am a software engineer, as folks who read this blog already know. I'm really interested in usability, mainly because I think too few software companies actually care about usability anymore. And I'm afraid that the problem has gotten worse with the advent of "agentic coding." It's easier than ever to "launch" an "app" (these scare quotes are doing a lot of work here) as a solo entrepreneur. Many people have pointed out that these apps are usually lacking things like scalability, security, and durability. Another thing that falls by the wayside for most of these apps is the user experience.

It would be ideal to hire a UX person to handle user experience, but the reality is that not everyone can hire someone. I led a user test for the Code for America National Brigade Network. Admittedly that sounds fancy, but it was a bunch of volunteers and me, and I just inserted myself into the project and said, "Hey, I think the site has some usability issues," and the longer term volunteers basically said "If you go away, you can do whatever you want." Which I interpreted as permission to go out and run a user test with a bunch of other civic tech folks. We learned a lot (although mostly learned that I was right 😎).

It is better to have a UX pro, but we can still get value out of some of the techniques that UX professionals use, even if we're not ourselves experts.

![A chart showing many types of user research. It's a bit overwhelming, but it charts various techniques, like A/B testing, eyetracking, and focus groups, along two axes: behavioral/attitudinal and qualitative/quantitative. User testing is squarely in the behavioral/qualitative quadrant.](/assets/2026/types_of_user_testing.png)
*[Christian Rohrer for NN Group](https://www.nngroup.com/articles/which-ux-research-methods/)*

These are some of the many types of user research.

I want to include this because I want to show how user testing fits into a vast landscape of user experience research, to show how deep you could go if you wanted to, and also to help explain what we're NOT doing.

This blog post covers only user testing, which is called usability testing on this diagram, and is in the upper left of the quadrant.  And so while there are lots of different types of research, user testing is behavioral and qualitative.

Behavioral: how people use the product.
Attitudinal: what they think about it.

What does that mean? It means user testing isn't market research, it's not a "contact us" form. It's watching what people do.

And user testing is qualitative. It's fuzzy, it's not hard numbers like a/b testing.

Quick aside:

#### If we have A/B tests, why do we need user testing?

A/B testing is great for gathering a lot of data about your website. 
It is very good at answering specific, quantitative questions based on a single hypothesis. 

- **If** I change this button color to **red**, do conversions go up or down?
- **Which** subject line will get **more** people to open my email?
- **If** I add another ad on this page, will my traffic go down? (Please stop adding more ad units.)

User testing is a little more open ended. It's good for answering questions like: 

- **can** visitors to the site successfully check out? 
- **where** do they encounter friction? 

More information on this can be found at [this blog post](https://www.invespcro.com/blog/ab-vs-usability-testing-friends-or-foes/).

## To sum up

User testing can be quite simple. TLDR: Get a person. Record them using your app.  Think about what problems they surfaced. Fix them. repeat.


## Sounds hard/time consuming/expensive

It can be! But:

- [Research shows]( https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) that testing with 5 users can uncover almost 80% of the problems in your design. 
- You could spend a lot (and I mean A LOT) of money here, and it would probably still pay dividends, but the user tests I've led have cost $0 plus my time. You may end up paying a couple hundred bucks out of pocket.
- You don't even need a finished website to start user testing (and in fact the earlier you start the better). You can do a user test with paper prototypes like these:
![A spread of paper prototypes for a pizza ordering app. You truly can just draw an app and people will instinctively know how to interact with it.](/assets/2026/pizza-paper-prototype.jpg)
Literally just draw your app and ask people to poke at it with their finger. You'd be surprised.

## Ok, let's try it

So let's say I have a website that sells purses. We're going to need to develop a question statement, or a hypothesis. So: Can people figure out from looking at the site that they can buy a purse here, and how easy is it for them to do that?

Or: I've just added a filter, how do people use it if at all?

Get some people together. One tester, you, maybe a few other members of your dev team. Ideally you're recording this, with their consent. On Zoom, or if in person, with your phone.

First things first, make sure they understand that THEY are testing the site, YOU are not testing them. I like to say something like, "There are no wrong answers here, and if you are struggling with any task, that's a reflection on us, not on you."

Then introduce the task. "I'm going to ask you to open a website on your computer, and have you attempt to accomplish a few things. I'll ask you to speak out loud to the extent that you can, and share your thought process as you go."

By the way? Ideally they're using their own device, because first of all, they're more comfortable, and second of all, let's be real, you have a better monitor than they do. 

So they load up the site on their own computer or phone. The first question I like to ask is "Without clicking anything or scrolling, what do you think this site is, and what can you do here?" They will HOPEFULLY answer with something like, "this looks like a shopping page for purses." If they can't answer that question, well, you already have something to work on.

Then give them a task. "Find a brown purse that you like that costs less than $200 and add it to your cart."

And then just watch what they do. Just sit there, as difficult as it sounds.

Can they find the search bar? Does "brown purse" bring up results? Can they filter by price? Are they ABLE to use the filter? Do they do the thing or do they sit there? Try to stay quiet while they do this, but if they're really quiet and not doing anything, it's absolutely OK to prompt them to speak out loud. "What's going through your head right now?"

If they complete the task, awesome! You probably still learned something from their behavior.

If they don't, at some point, you implement the mercy rule. A frustrated tester isn't going to give you valuable information past "this is incredibly frustrating." Just end the task and move on.

### Tips ###

- You cannot remind a tester enough, especially if they're not a "professional" tester, that they're not the ones being tested. If they feel like they're "failing" at a task they're likely to get frustrated.
- Stick to one thing at a time. Just "find a purse," not "tell me everything that's going through your head when you shop for purses, what websites you prefer and why, while also using our website."
- Ask open-ended questions, not closed ones. 

  As a reminder, closed-ended questions are ones that can be answered with a simple yes or no, while open-ended questions are ones that require more effort to answer.
  
  So instead of: "Did you find that difficult?" which can only be answered with a yes or no, ask, "How easy or difficult was that?"
  
  Instead of, "Did you notice the filter options?"  maybe "How did you decide how to narrow down your choices?"

- Word your tasks carefully. It's best not to use the exact wording of the feature in your question. In other words, don't say "filter the purses by color", say "find a brown purse."

- Believe what they do, not what they say. People are trying to please you so they'll probably say "yes it was easy" even if it took them 10 minutes to find the search bar. Actions speak louder than words, yadda yadda.

## What do you do with all this information?

Let's say 2/5 of your users told to find a brown purse used the color filter, and the other three didn't. Why?

- Did they notice the filter? They hovered their mouse over it, or mentioned it? Or didn't?
- How did they find the right thing without it? Was the filter not necessary?
- Did they not need the filter because you only have 3 items on the page so there's no need to filter further?
- Did they not see the filter because it's in a weird place?
- Was the filter so huge that it was too overwhelming to use?
- Were there technical usability issues? ([Mega menus](https://blog.logrocket.com/ux-design/mega-menu-design-examples/), looking at you)

Come up with a new hypothesis based on what your testers did, make changes, test again.

## How to find people

Ask.  Start with friends and family, preferably ones who haven't already seen your product.

If you are a nonprofit, you might find people willing to donate their time. Check your volunteer networks.

If you are for-profit and you've used up all your friends and family, you might need to pay people something. The going rate for an hour of time is roughly $60, in my experience, although everything's so expensive now. Finding people directly is going to be *significantly* more economical than going through an agency, but you have to do more of the legwork.
 
Ideally you're pulling from your target market. If your app is for nurses, maybe try your local nursing association? "We're looking for nurses who have at least 5 years of experience to give us an hour of their time for a paid study." Try Linkedin professional groups, Slack communities, etc. 

If your target market is 'average person who buys purses' you're in luck, though, because you can just find anyone, and it's going to cost less money but maybe take a little more time.

Just go to your local coffee shop, the hipster one that doesn't do online ordering, during the morning rush. Bring a tablet with your site on it. Find the person farthest back in line who isn't engrossed in a podcast and say, "If you help me with this thing, which will take less time than it takes to get to the front of the line, I'll give you a $5 gift card to this coffee shop."

They frequently say yes, since they're already in line, you're not taking any more of their time. This is a really cheap way to get some quick tests done. Of course, you don't have an hour in this scenario, so make sure to come up with something that can be done quickly.

## Some things you might learn

Here's where I tell you what results you'll get. Just skipping the testing and reading this blog post is the cheapest way to do user testing.

But seriously, these are the things I've noticed, and I suspect they might be universal patterns.

- **Nobody knows what your site is**. You know what it is because you've been immersed in it every day. Nobody else will be able to tell what it is, especially, I'm looking at you, nonprofits that just have a bunch of smiling people on the homepage and I have to click through seven menus to get to "about us". You should pretty much always ask "what is this site, who is it for and what can you do here," just to confirm that everyone's on the same page.

- **All buttons should be bigger**. This is only half a joke, but like, designers love stuff to be small and compact, and I agree, it does look better, but once you see someone actually using your product, it turns out most people just want buttons that are huge. Watch how people navigate your product and I bet they'll mis-tap at least once and get frustrated.

- **People notice all the stuff you've stopped noticing.** The uncomfortably long loading spinner, the slightly janky repaint... Again, if you're really close to a project maybe you stopped seeing these things. People with fresh eyes will notice. Maybe you're not interested in fixing these little things. That's actually valid, you're testing a specific question like, "is the navbar easy to understand?" But if there's enough jank, people are gonna get frustrated, so keep an eye their level of anxiety. Because an anxious user is not a user who's going to stay on your site a long time.

But the thing that I can guarantee will happen is you will be surprised by something a user does.

To quote from the awesome Jakob Nielsen:

> "Many ... have described the almost religious effect [when people] see with their own eyes the difficulties perfectly normal people can have using supposedly "easy" software."

So you may experience these takeaways for yourself or you may learn something else. But after you've done this a few times you will almost certainly have learned something useful.

But by the way, even if YOU have learned something useful, maybe you now need to convince your boss to implement it, if you're not such a small organization that you are the boss.

I don't have a lot of great advice here, I'm afraid; but the usual stuff about speaking your boss's language applies here.

You're not saying "we need to redesign the homepage because it takes 20 seconds to load and with a new framework we can....", you're saying "We should consider redesigning the homepage because our visitors are leaving before buying anything, and our user tests showed that they found the homepage difficult to use."

Also, let your boss watch a user testing experience (or a recording). Then she can have the same religious experience that you did the first time you watched someone struggle with your checkout page.

The fact that you did these tests for less than the cost of a single sales dinner helps, too.

I hope you've enjoyed this foray into the wild world of DIY user testing. This is something I love talking about and writing about, even though I haven't gotten to actually do it lately. I hope you too will find satisfaction (or a religious experience) after trying these techniques out.

What's the most surprising thing you've discovered during a user test? Or what was the moment you realized you needed one? [Drop me a line]({{site_baseurl|relative_url}}{%link about.md %}) and let me know.
