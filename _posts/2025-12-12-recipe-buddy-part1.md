---
layout: post
title: "Building a Cookbook With Python, for Reasons (part 1)"
categories: stuff-i-made
excerpt_separator: <!--more-->
project: "The Brookland Dish"
description: Spinning up a FastAPI backend and discovering the complicated world of email webhooks.
image: /assets/BrooklandDish.jpg
---

## 📖 + 🐍 = ?

*Note: This is a longer writeup of the project I presented at PyLadies 2025. If you want the bite-size version, [watch it here](https://www.youtube.com/watch?v=A_oU7d_H8oM).

I'm part of a monthly potluck that organizes meetups over email, then meets in person to eat delicious vegan food. (I'm not vegan, but I love any excuse to try new recipes and eat more plants.) Occasionally, potluck members will email around a link to the recipe they used or are planning to use.

![A pretty normal, boring email, where the sender says, "I'm thinking of bringing curried lentils with sweet potatoes and hazelnuts."](/assets/brooklanddish-emails.png)

Pretty common thing, but I wanted to capture these recipes in a more permanent way than a link to a random blog in a mailing list archive. Link rot is a thing, plus it's just not very fun to have to search old messages and try to remember when that delicious soup recipe was sent around -- was it this year or last?

I had an idea pop into my head at over the summer (I love when these things happen) that I could automatically post recipes to a new blog, when they were posted to our listserv. So then I spent the next two weekends making it happen.

I'll discuss how I built it in a series of posts (the writeup is far too long for a single post). Today's post is about the overall stack, as well as the FastAPI backend.

## The stack

We need an email address that will serve as the "listener" to notice when new recipes are posted and do something with them. This could be anything but I may as well buy a domain and then I can host the blog there as well. So I went to Cloudflare and bought `brooklandrecipe.party`.

We also need a backend that can do the "something" when a new email comes in. Based solely on the fact that the first recipe-parsing library I found was written in Python, I chose to use FastAPI, which is a lightweight Python backend. This turned out to be an excellent choice.

We need a way for the email listener to talk to the backend. I found [ProxiedMail](https://proxiedmail.com), which has incoming email webhooks.[^1] And it's got a free plan. Fantastic. Now when anyone sends an email to `incoming@brooklandrecipe.party`[^2], we can make a POST request to our new API.

And we need a frontend, preferably one that updates with (minimal) intervention from a human. Jekyll with Github Pages is great for this. Posts are built in markdown and upon a successful merge to `main` the site automatically will build and deploy.

Basically, we need this:
![A flow chart showing the following steps, in order: Incoming email->POST recipes->email contains a url?->URL contains a recipe?->Create new post from template](/assets/brooklanddish-miro.jpg)

Those are all the parts! Let's see how they fit together.

## The email and the backend

As previously stated, I set up `incoming@brooklandrecipe.party`[^3] to post back on receipt of an email. We can inspect the shape of the payload before doing anything, by instead setting the postback destination to a free[^4] URL on webhook.site. This shows us the shape of the payload, which I have shortened by removing the boring stuff:

```json
{
  "id": "A48CF945-BD00-0000-00003CC8",
  "payload": {
    "Content-Type": "multipart/alternative;boundary=\"000000000000a4a98d063b045239\"",
    "Date": "Mon, 28 Jul 2025 17:53:20 -0400",
    "Mime-Version": "1.0",
    "Subject": "test",
    "To": "news-e12c76@proxiedmail.com",
    "body-html": "<div dir=\"ltr\">hello</div>\r\n",
    "body-plain": "hello\r\n",
    "from": "Rachel Kaufman <my-email>",
    "recipient": "news-e12c76@proxiedmail.com",
    "stripped-html": "<div dir=\"ltr\">hello</div>\n",
    "stripped-text": "hello",
    "subject": "test"
  },
  "attachments": []
}
```

This is going to post to our backend REST API built with FastAPI. FastAPI uses Pydantic to define types under the hood, so we can design our endpoint's desired input like:

```python
class EmailPayload(BaseModel):
    Date: str
    from_email: str = Field(..., alias="from")
    stripped_text: str = Field(..., alias="stripped-text")
    recipient: str = Field(..., pattern=pattern)
```

Notice those "alias" fields; this is a cool FastAPI/Pydantic trick to change any string input to valid python. (`stripped-text` isn't a valid name for a variable in Python, even if it's valid as a JSON key. And I aliased `from` to `from_email` just so I had a clearer picture of what that variable represented. Although now I think I should have called it `sender`....Oh well.)

The actual logic is pretty simple. We need to get the text of the email, check if it contains a URL. If it does, we need to check if that URL is for a recipe (and isn't just a link found in someone's signature for example). If it is a recipe, we need to scrape the recipe data, create a Markdown file with the recipe data in it, then send that Markdown file to Github in the frontend repo.

Putting it all together it looks like:

```python
@app.post("/my-route")
async def parse_message(message: IncomingEmail):
    message_body = message.payload.stripped_text
    message_sender = message.payload.from_email.split(" ")[0]
    recipe_url = contains_url(message_body) #a pretty simple regex that returns the first match if found or None if not
    if not recipe_url:
        return {"message": "no url found"}
    recipe = parse_recipe(recipe_url) #uses the recipe_scrapers library and returns a dict
    if not recipe:
        return {"message": f"no recipe found at URL {recipe_url}"}
    template, filename = generate_template(recipe, message_sender) #creates a blob from the template and dict
    make_github_call(template, filename) #actually makes quite a few github calls
    return {"message": "ok"}
```

Let's look at a few of these methods in more detail. I'll skip over `contains_url` as it's pretty boring.

`parse_recipe` is also pretty simple - it just grabs the URL, resolves it, and uses the `recipe_scrapers` library to get the recipe data, such as its title, cook time, ingredients and instructions. Most recipe websites use standardized formats, codified by [Schema.org](https://schema.org/Recipe) so this library supports a good number of sites (but not all).

Once we have our dict of parsed values, we can inject them into a Markdown template for use by Jekyll. Which I'll discuss at a later date.

[^1]: SO MANY services that claim to have "email webhooks" only have webhooks for message delivery events, which honestly makes sense as it is probably the much more frequent use case. But I just want to make a POST request when a new email comes in.
[^2]: Not the actual email address.
[^3]: Still not the actual email address.
[^4]: Each unique webhook.site URL can respond to 100 post requests. More than that and you'll need to pay up.
