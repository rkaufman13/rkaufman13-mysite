---
layout: post
title: Why I'm One of the Last People to Still Visit StackOverflow
categories: musings
excerpt_separator: <!--more-->
description: I didn't realize I was such an outlier.
---

We've all seen [the graph](https://meta.stackoverflow.com/questions/437921/how-does-the-continued-decline-in-posts-since-may-25-influence-our-interpretati). Fewer questions were asked on Stack Overflow in May 2025 than in September 2009, which was three months after the site launched.

!['The graph'. It's bad, y'all. Question volume peaked in 2013 at over 600,000, and has been on a fairly steady decline since then.](/assets/stackoverflow-depressing-graph.png)

That should be **concerning af** for anyone who writes code. Yes, LLMs can answer many (not all) questions about syntax, usage, and even spit out paragraphs on architecture and design suggestions that sound confident, and are probably right, or close enough to right, most of the time. But these models got these answers from sites like Stack Overflow in the first place, and with almost no new content added, I wonder what will happen when people have truly novel programming questions where the answers haven't been first answered by a person.

I'm one of the rare people who still goes to Stack Overflow. Not to post new questions, but I was never much of a question poster there anyway. Like many people, I found I either didn't get an answer, or got yelled at, a problem SO has been dealing with for many years prior to the advent of LLMs.

So I don't post new questions (or answer existing ones). But I still find reading answers on SO very valuable.

The reason is _context_.

![A beautiful shelf of old-fashioned books, presumably in a library of some sort.](/assets/library.jpg)

Context clues in a library might include where the book is shelved or how old the cover looks. If I'm looking for up-to-date programming information I'm not going to reach for those gorgeous leather-bound spines. If, on the other hand, I'm looking to become an isekai protagonist, I'm gonna find the oldest, crustiest book on the shelf. (A girl can still dream..)

Anyway, context clues on Stack Overflow include:

- What's the writing style of the person who posted the question? If they're typing like a high schooler, they're probably a high schooler trying to get their homework done. Which to me implies that _maybe_ they're asking an [X-Y question]({{site_baseurl | relative_url}} {%link _posts/2024-10-18-getting-unblocked-faster.md %}) or otherwise are coming at a problem from the wrong angle. If my question looks like theirs, I may need to rethink my premise. (Or not, there are lots of smart high schoolers, and also lots of people who type like high schoolers but aren't. And SO questions and answers can both be edited. These are context clues, not binaries.)

- What's the writing style of the person who _answered_ the question? Did they post a quick, copy-pasted (or LLM-generated) answer for the reputation, back when some people cared about rep, or is there a longer explanation of _why_ the solution works? The shorter the solution the less likely it is to work for my specific use case, in my experience.

- How old is the question and answer? Language fundamentals ("how do I do X in Y") don't change that quickly (although they still do -- look at python2 vs python3), but a question about the specifics of a framework like React can go out of date within a year or two.

- How many people are arguing in the comments section? This is both a source of amusement and a yellow flag to pay attention to the answer, because there may be a drawback that the OP hadn't considered.

I like context on github issues as well. If I'm having trouble with a library, searching old issues can be a good way to find information. Sometimes the issues are marked as addressed, and then I can deduce whether my version of the library has the feature I'm looking for, and sometimes the issues are closed as "won't do" with a workaround suggested. Then I'll see who posted the workaround, and, again, how old the workaround is.

With LLMs you get none of this context, you just get an information-shaped blob. A very confident, information-shaped blob. Is it right? For problems like "how do I do X in Y," probably. For more complicated problems? It might be "correct" (or it might not; I spent some time arguing with Claude the other day as it continued to insist that I was providing an incorrectly shaped payload missing a parameter that was clearly right there), but even if it is, is it the optimal solution?

Without the debates and the context clues, I'm not sure. So if I just want to copy and paste something without understanding it, a LLM probably ties with searching SO and copying the first thing that looks right. If I want to learn, I need context.
