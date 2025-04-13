---
layout: post
title: "Some Tips for Working With the Google Sheets Java SDK"
categories: things-i-learned
tags: google gcp java
excerpt_separator: <!--more-->
description: And some unanswered questions.
---

At work, I've been working on a project that involves reading and writing data to and from a Google sheet. One could argue about the wisdom of using Google Sheets to hold any data, but for the sake of this post (and my sanity) let's assume that the business requirements to use Google Sheet are watertight.

So I have to be able to talk to Google Sheets through my Java service, and of course Google has  a [Sheets SDK](https://developers.google.com/workspace/sheets/api/quickstart/java) that we can use. Their [quickstart tutorial](https://developers.google.com/workspace/sheets/api/quickstart/java) assumes a different method of access/authorization than I expect to use, but that's okay.

For my purposes, I needed to create a project in my company's GCP account, and a service account that had access to that project. That gives me a set of credentials in JSON that we can store anywhere (we're using AWS paramstore, because this is a two-cloud-provider kinda project!), **but in order to access a specific sheet we also have to share that sheet with the service account**. I bolded that because I've forgotten that step *multiple* times throughout the lifespan of this project. 

Repeat: the service account credentials, even when scoped to SPREADSHEETS:ALL, still cannot access individual spreadsheets in your organization's workspace *unless you share the spreadsheet with them.* Seems kinda cray that we have to treat the service account like a person in order to access resources, but I guess Google ended up picking a person-based model years ago and now they're probably stuck with it.

![A faked share screen showing my personal Gmail account sharing a spreadsheet with a fake Google service account.](/assets/gsheets-share.png)
(This is not a real example.)

Once you've shared your sheet you can start talking to it in Java. I built credentials like this:

<!--more-->

```java
GoogleSheetsAuthDto dto = googleSheetsAuthConfig.createAuth();  
GoogleCredential.Builder builder = new GoogleCredential.Builder()  
        .setServiceAccountPrivateKey(dto.getPrivateKey())  
        .setServiceAccountPrivateKeyId(dto.getPrivateKeyId())  
        .setServiceAccountProjectId(dto.getProjectId())  
        .setServiceAccountId(dto.getClientId())  
        .setJsonFactory(JSON_FACTORY)  
        .setTransport(httpTransport);  
return builder.build().createScoped(SCOPES);
```

The `createAuth` method reads properties in from a .properties or config file and parses the private key string into an actual private key. Then we can set those values in this credentialBuilder. (This method is officially deprecated, per Google, but it still works and is simpler than the other options...) `SCOPES` will be the permissions you want your credential to have, in my case "SPREADSHEETS", but you can scope the credential to other services, keep it read-only, etc.

Once you've created the client, you can do things like:

```java
final ValueRange values = new ValueRange().setValues(List.of(valueList));  
String updatedRange = sheetsClient  
        .spreadsheets()  
        .values()  
        .append(spreadsheetId, range, values)  
        .setValueInputOption(VALUE_INPUT_OPTION)  
        .execute()  
        .getUpdates()  
        .getUpdatedRange();
```

This long chained method takes in your spreadsheet ID, a range (in A1 notation) at which Google will  start searching, and a new set of values. Google will find the next empty row in the sheet, appending your values to the next empty row, and returning the range that was updated. In my case, I only care about the row that was updated, so then I use a regular expression to pull out the numerical part of the row and return that. (Not shown here.)

If you want to skip any columns when adding a new row, lucky you, you have to construct your `valueList` object with nulls in it, like so:

```java
List<Object> values = new ArrayList<>();  
values.add(myFirstValue); //will be added to column A, row {}   -- whatever the next empty row is
values.add(null);  //will skip column B
values.add(mySecondValue); //will be added to column C, row {}
```

It's clunky, but it does work.

I do wish that there was an easier way to map columns to values. In other words, if I have a spreadsheet with the header row First Name, Last Name, I should be able to say "append 'John' to the next empty row in the 'First Name' column", but that's yet another argument for not using Google Sheets as a database, and we've already established that we're doing that here :)

![Jim Carrey in 'Dumb and Dumber' shouting 'We're really doing this!' I have not seen this movie.](/assets/dumb-and-dumber.gif)

So what else did I learn from this project?

- This SDK is super hard to write tests for. Google provides a mock HTTP server so if you want you can mock the low-level requests, but that's a pain; you can mock the client itself but there are so many chained methods that need mocking too that the unit tests quickly become unwieldy. I thought about creating my own test fake but there are also just so many methods in the SDK that there would be a lot of boilerplate there. I may go back and do it anyway because the existing solution is driving me batty. There aren't a lot of people posting about this on StackOverflow, etc., this is a new use case for my company so I don't have any internal experts to turn to, and I even tried asking Copilot for some suggestions, and it spat out the same smelly code I'm trying to avoid using. If anyone reading this has a better suggestion, please shoot me a note!
  
- Append over edit, 100%. If your need requires updating rows, can you somehow change it to be a read-only stream of logs? To update a row, you've got to keep track of the row number that you want to change or somehow grab the whole sheet (or a portion of the sheet) and filter down to the row you want. This can be slow, subject to rate limiting by Google, etc. Whereas append is as easy as the code above.
  
- PLEASE remember to share your sheets with your service account :) I've forgotten so, so many times, so this is really a note to myself.
