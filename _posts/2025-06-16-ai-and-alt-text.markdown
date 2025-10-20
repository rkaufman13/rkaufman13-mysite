---
layout: post
title: "What I Learned This Week: AI and Alt Text (Don't Do It)"
categories: things-i-learned
tags: accessibility
excerpt_separator: <!--more-->
description: The tech is not yet ready to replace people.
image: /assets/alt-text-pizza.png
---

![A woman typing on her laptop. The text reads: "<img src=pizza.png alt='a delicious oozy slice of pizza'>".](/assets/alt-text-pizza.png)

For those of us who are sighted, it is easy to forget that alt text is a necessity for navigating the Internet for the millions of blind individuals who use screen readers. Not to mention, there are still, believe it or not, Internet users who _do not load all images by default_, whether to avoid some types of tracking or because their internet is spotty/unreliable. So if you're reading this and ever work in the frontend, hopefully you are remembering to include alt text. (Thankfully, this blog generates its static files from Markdown, a language in which it's easier to add alt text to images than not. But I'll be the first to admit I could write _better_ alt text.)

But isn't writing alt text _so much work_? What if we let an AI write it for us?

Last week, my colleague gave an excellent presentation about the possibility of using AI to generate alt text. This is something that a number of websites are doing (see [describeimage.ai](https://describeimage.ai), [imageprompt.org/describe-image](https://imageprompt.org/describe-image), [aitools.inc/tools/ai-alt-text-generator](https://aitools.inc/tools/ai-alt-text-generator), [describepicture.org](https://describepicture.org), and many, many others--I would assume that 99% of these are just wrapping an API call to ChatGPT). 

I believe gen-AI tools are built into a number of CMSes as well. For example, [here's a blog post](https://pivot.umbc.edu/news/post/143089/) talking about how the edtech software Blackboard will flag images without alt text and offer to generate descriptions of the images, using Microsoft genAI tech.

However, the general consensus is that this tech is not yet ready to replace humans.

My colleague demoed a couple of images that are relevant to people who work in marketing. One of them was:

![Nike logo](/assets/Logo_NIKE.svg.png)
*We all know what this picture is, right?*

An AI alt-text generator described this as "a simple black checkmark on a white background," whereas humans would probably prefer this to have the alt text "Nike logo" or simply "Nike".

My colleague also showed a product image of a shampoo bottle on a beach. Since we work in marketing, our clients use a lot of product images! AI described this (fake) product image as something like, "A white bottle, labeled 'shampoo', standing upright on a sandy beach." Better alt text would be the name of the product, like "Ocean breeze shampoo."

Especially if the image is used as a clickable link (say in an email where you want people to buy the shampoo). If an image is used as a link, most (all?) screen readers will use the alt text as the link, so a long, flowery description is not useful here.

AI image descriptors also miss important cultural context, as shown in [this article](https://digitalaccessibility.unc.edu/2024/11/26/ai-and-digital-accessibility-whats-up/) from UNC's digital accessibility office, showing an example where a Maori dancer performing a ceremonial _haka_ dance is described as "a person with his tongue out."

That said, not every website does alt text well at this time. I found [this exercise](https://cs.clarku.edu/~cs103/class/ai-generated-alt-text/) from Clark University's "Introduction to Societal Computing" (what a wonderful class title, can I audit?) in which students are asked to compare AI-generated alt text and human generated alt text from three websites: a news site, a large nonprofit, and any third site. In the example given, the professor compares alt text on the New York Times' website, Wikipedia, and Clark University's own site.

I'll let you [read the outcomes for yourself](https://cs.clarku.edu/~cs103/class/ai-generated-alt-text/) but the TLDR is, unsurprisingly, large websites do a good job of writing descriptive alt text that generative AI cannot outperform, but smaller websites often have useless or no alt text, in which case a generative-AI-written caption might be a slight improvement. But there's another way to improve alt text, which is to write it!

I couldn't find a lot of takes on this topic from screen-reader users themselves. The general consensus seems to be that some (bad) alt text is better than no alt text.

However, I was hoping to find posts such as, "My favorite website went from having good alt-text to mediocre alt-text overnight, and I suspect they're using AI", or "My favorite website went from having no alt-text to mediocre alt-text overnight, and I suspect they're using AI." The lack of such takes leads me to think that this technology isn't widespread enough yet for people to have noticed.

If a website's images have _no_ alt text, some screen readers and other software can still identify images, using their own built-in software. I believe this feature is built into new versions of the screen-reader JAWS, for example. But this software isn't necessarily any better at identifying images, and can often be worse. Users report "hallucinations" and bugs, in the forums I found.

Supporters of AI-generated alt text say that if your choice is between literally no alt text (forcing users to rely on their own software, if they have it) and alt text written by a generative AI and approved by a human being, the latter is better. I guess that's true, but only barely.

My take? As web developers, we can do better than outsourcing image descriptions to generative AI.

### Resources

- [Google's guidelines for writing helpful alt text](https://developers.google.com/tech-writing/accessibility/self-study/write-alt-text)
- [Alt text as poetry](https://alt-text-as-poetry.net/)