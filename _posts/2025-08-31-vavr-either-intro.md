---
layout: post
title: "An Intro to vavr's Either"
categories: things-i-learned
excerpt_separator: <!--more-->
tags: java functional-programming
description: There are many guides to working with Either in Java on the web. This one's mine.
image: /assets/apple-to-orange.jpg
---
![A pair of hands, one holding an apple, and another holding an orange.](/assets/apple-to-orange.jpg)
*Either an orange or an apple would be delicious.*

[`Either`](https://www.javadoc.io/doc/io.vavr/vavr/0.10.0/io/vavr/control/Either.html) is an incredibly useful tool in a Java programmer's handbook, one that brings functional programming control to Java.

If that didn't make sense, I get it. Either is much easier to use, to me, than to explain.

### What `Either` does

An `Either` is used when you want to return one of two types, typically a failure or a success. If an operation succeeds, we don't really see any benefit of using Either. But if it fails, instead of throwing an exception and catching it, we can transform all our exceptions into a predictable failure class, which reduces boilerplate code.

Here is a wonderful example from [Yuri Mednikov on Medium](https://yuri-mednikov.medium.com/either-implementation-in-vavr-library-b137436fe705):

>From a technical point of view, _either_ is a container, that can hold two values — one for successful result and one for failed result. Imagine, that you write a code, that deals with file reading — you use a file service abstraction, that your colleague wrote for you. You don’t need to know how it works, you just call a method, that returns a content of the file. Yet, you know, that it may throw an exception, if file does not exist. Take a look on the following code snippet:
>
>
> ```java
> FileReadService service = new FileReadService();  
> try {  
>     String content = service.readFile("no-such-file.txt");  
>     return content;  
> } catch (BadFilenameException ex){  
>    System.out.println("No file found");  
>     return readFromCache();  
> ```
>
> Imagine, that in future, the technical design will require the `FileReadService` to determine also other error cases. The number of `catch` clauses with increase… With `Either` type you can refactor this code as following:
>
>
>```java
>FileReadService service = new FileReadService();  
>String content = service.readFileSafely("no-such-file.txt").getOrElse(readFromCache());
>```
>
> This style helps you not only to eliminate try-catch blocks, but also to specify a single entry point for all errors to make them to recover from a cache.

The [full article](https://yuri-mednikov.medium.com/either-implementation-in-vavr-library-b137436fe705) is a pretty good read, check it out.

### Getting fancier

Once you've gotten the hang of basic Either usage, know that the real power of Either comes from chaining results. With the `map()` method we can transform an `Either.right` (which is by convention the happy-path case) any way we choose, and with `mapLeft()` we can transform an `Either.left` (by convention the error path case) in the same way.

Imagine we have a service that queries for a row in a database and maps it to a database object. Then, since we don't want our db models to leak into the rest of our service, we convert it to a service-level DTO. Without Either, it might look something like this:

```java
public MyDto findById(int id){
    try {
        MyDbModel result = repo.getById(id);
        if (result !=null){
            return mapToMyDto(result);
        }
    return null; //which will likely cause an error upstream
    } catch (JdbiException e){
    throw e; //or return null, which will cause another error upstream
    }
}
```

Pretty simple, but let's walk through it.

The code asks our repo class to find something by id. If it's found, we'll assume it's mapped to our MyDbModel class. If the result is null, we have a problem. Similarly, if the database throws any errors, all we can do is try to catch them.

With Either, our code can look like this:

```java
public Either<Problem,MyDto> findById(int id){
return repo.getById(id).map(this::mapToMyDto);
}
```

It's not just 10 fewer lines of code to write, it's also, I would argue, easier to read. BTW, in this case Problem is a custom [pojo](https://en.wikipedia.org/wiki/Plain_old_Java_object) that has a type, a message, and of course anything else we would like to add. 

In this example, we are also assuming that the repo method also returns an Either. If it's a left, it is returned up the call stack until something determines what to do with it. If it's a right, the model is transformed into a `MyDto` using the same mapper class.

### My current favorite `Either` method: `sequence`

One very cool method that comes with `Either`, and one that I find myself using more lately, is `sequence`, which transforms a list of `Either`s into an `Either` of lists. If that sounds confusing, imagine this example:

```java
public Either<Problem,<List<String>>> createStrings(List<String> inputs){
```

Actually, wait, interruption time - I don't know what this contrived example is supposed to do either. Let's pretend we're transforming these strings in a way that is possible to throw an error, but the transform method catches all errors and transforms them into `Problem`s (our custom, predictable `Either.left`.). That would look like this:

```java
public Either<Problem,<List<String>>> createStrings(List<String> inputs){
    List<Either<Problem,String> results = List.of();
    for (String myString: inputs){
        results.add(performRiskyOperation(myString));
    }
```

At this point we have performed some operation on every string in our list of strings, and added each result to a list to hold the results. Because `performRiskyOperation` returns an `Either<Problem,String>`, each item in the list is *either* a `Problem` or a string. In other words, if we were to inspect our list, it might look like this:

```java
results.get(0); //Left(Problem.UnsupportedOperation)
results.get(1); //Right("hello");
results.get(2); //Right("world");
results.get(3); //Left(Problem.Null)
```

 But what we really want is all the strings, if the operation succeeded each time, or an error, if it didn't. That's where `sequence` and its cousin `sequenceRight` comes in:

```java
public Either<Problem,<List<String>>> createStrings(List<String> inputs){
    List<Either<Problem,String> results = List.of();
    for (String myString: inputs){
        results.add(performRiskyOperation(myString));
    }
    return Either.sequenceRight(results).toJavaList();
}
```

That one-liner turns the list of Eithers into one Either, which contains either a Problem, or the full, happy-path result (the list of strings). (`toJavaList()` is needed if you want to turn the `Seq` object, which is list-like but not a list, into a regular ol' list.) `sequenceRight` will return a single Problem (the first one it encounters) or the full list; regular old `sequence` will return a list of Problems or the full list of strings. The cost is, well, the pretty ugly method signature of `createStrings`, but when you are working with lists and Either, it is a small price to pay.

There are many other methods available within Either, and I hope you'll [read the docs on them here](https://www.javadoc.io/doc/io.vavr/vavr/0.10.0/io/vavr/control/Either.html).
