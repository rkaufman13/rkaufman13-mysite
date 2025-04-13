---
layout: post
title: Save Time With Postman's Pre-Request Scripts
categories: things-i-learned
tags: api js 
excerpt_separator: <!--more-->
description: Postman is a super-powerful tool and this is just one of the many things I didn't know it could do.
---

![A screenshot of the Postman interface.](/assets/postman1.png)

Postman is an incredibly powerful tool for prototyping and testing APIs. If you ever find yourself making any kind of API request to any service (regardless whether it's one you built or one you use), I really think you should be using Postman.

In this post I'm going to share how to use pre-request scripts to make Postman even more powerful.

One common pattern in many web APIs is exchanging an API key for a token. In short:

A developer generates an API key once. Then, using that key (and possibly other secret credentials), they can call a token endpoint, which reads the key and returns a short-lived bearer token. The bearer token usually expires after a short time, such as an hour, at which point the token must be refreshed.

As an example, take a look at the [docs for Shopify's API]( https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/token-exchange):

> Step 1: Ensure you have a valid session token.
> Your app's frontend must acquire a session token...
>
> Step 2: Get an access token.
> If your app doesn't have a valid access token, then it can exchange its session token for an access token using token exchange.

In this scenario, a developer makes a POST request to `https://{shop}.myshopify.com/admin/oauth/access_token` with her app's API key and a few other secret parameters, and receives back this response:

```json
{
  "access_token": "f85632530bf277ec9ac6f649fc327f17",
  "scope": "write_orders,read_customers",
  "expires_in": 86399,
  "associated_user_scope": "write_orders",
  "associated_user": {
    "id": 902541635,
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@example.com",
    "email_verified": true,
    "account_owner": true,
    "locale": "en",
    "collaborator": false
  }
}
```

She now has an access token with two scopes that expires in 86399 seconds, or just under one ([normal](https://swizec.com/blog/a-day-is-not-606024-seconds-long/)) day.

If you're a user of whatever this Shopify app is meant to do, all this happens invisibly, under the hood. But if you're a developer testing against the Shopify API, you probably have to do this token exchange daily, manually. First make a POST request to the token endpoint, then retrieve the result, then paste the token into the API call you actually want to make.

And many services provide tokens with much shorter expirations -- an hour or even a few minutes.

You could save a separate request in Postman and remember to hit the token endpoint before you make a new request, or you could use a pre-request script to chain the two calls together. Here's how it's done.

<!--more-->

The pre-request script section of a request or a collection[^1] contains (a stripped-down version of) Javascript that executes before every request. So if we need to make a request before we make a request, this is a perfect use case!

Here's an example. This does not use Shopify's API, this is a different API that I use at work, so you'll notice the shape of the request payload is a bit different.

We write code like so:

```js
pm.sendRequest({
    url: pm.globals.get("token_url"),
    method: "PUT",
    header: {"Content-Type": 'application/json'},
    body: {
        mode: 'raw',
        raw: JSON.stringify({
            param1: "whatever",
            param2: ["whatever","whatever"]
            }) 
    }
}, function (err, res) {
    pm.collectionVariables.set("auth_token", res.json().access_token);
    console.log(`got auth token: ${res.json().access_token}`)
    });
```

This calls a URL that we've saved as a variable (as a global; we can also save it as a collection variable or local to the request), passing in our secret, which is saved as another variable in the collection, meaning it's available to all requests in the same collection.

The result comes back as JSON, with a shape like:

```json
{
    "access_token": "secret token",
    "access_token_id": "also secret",
    "token_type": "Bearer",
    "expires_in": 3600
}
```

Then we retrieve the value we want from the JSON and set it to the value of a third variable, which is the one we've set as our bearer token in the auth tab.

![The Postman UI showing the "Authorization" tab with a variable set where the bearer token should be.](/assets/postman.png)

Presto! Now every time we make this request, Postman automatically runs the pre-request script that  refreshes our token and saves it so we're always authenticated. We've gone from two button presses to one, thereby doubling our efficiency as developers :)

[^1]: GRPC collections currently cannot contain pre-request scripts, which is a major bummer. (GRPC collections in Postman have seemed to be a bit of an afterthought ever since the team released GRPC support a couple years ago, alas.) There is a [two-year-old open issue](https://github.com/postmanlabs/postman-app-support/issues/11699) about it, and a very hacky workaround suggested by the team in the comments. Maybe this will be the year!
