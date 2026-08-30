---
layout: post
title: "A Better Way to Test Object Equality in Java Unit Tests"
categories: things-i-learned
tags: java junit assertj testing
excerpt_separator: <!--more-->
description: Testing for object equality can be painful, but it doesn't have to be.
---

![A vintage-looking set of grocery scales. They are roughly equally balanced.](/assets/2026/equality-scales.jpg)

This is mainly a note to myself because I'm pretty sure I've "learned" this material at least twice before, then forgotten it. Maybe the third time (and writing it down) will help it stick.

I have been working on a project adding some new fields to a Java object. Long story short, the model was created to work with a single type of entity, and we're now abstracting that model to work with more than one entity. Not really important, what's important is how frustrating the unit tests have been.

```java
@Test
void insertIntoDb(){
Person person = new Person(id, name, age .... createdAt, updatedAt);
insertIntoDb(person);
Person actual = getFromDbById(id);
assertEquals(person,actual)
}
```

If one of the 20 attributes of this Person mismatch, you get a huge wall of text:
```java
AssertionFailedError:
expected: Person {
id=123,
name=John doe,
age=32,
...
...
STILL GOING...
updatedAt=2026-07-13T10:27:07.131423
}
but was: Person {
ugh just stop
}
```
This is not ideal. Some IDEs make parsing this easier, but for some godforsaken reason, my test was only failing in CI and not locally. (Do not ask me why. I do not know.)

To make things worse, `assertEquals` DOES use the object's overridden `.equals()` method, if there is one (as it should), but the test failure message spits out the object's `.toString()` output. If you're, for example, ignoring timestamps when doing equality comparison, but you still see them in the test failure output, that can be pretty annoying/confusing. I went back to my class's `.equals()` method at least twice to make sure I wasn't losing my mind.

## There's gotta be a better way!

![A short GIF from the 'Friends' episode where Joey says "There's gotta be a better way!"](/assets/2026/joey-better-way.gif)

You're so right, there is!

If we're using [AssertJ](https://www.baeldung.com/introduction-to-assertj) instead of JUnit's assertions, there's this pattern:

```java
assertThat(actual)
.withRecursiveComparison()
.isEqualTo(expected);
```

This "walks the object tree" and compares every field in the object. If a mismatch is found, you get a much more useful error message:

```bash
Expecting actual:
    ...
to be equal to:
    ...
when recursively comparing field by field, but found the following difference(s):
field/property 'address.zipCode' differ:
  - actual value  : "02139"
  - expected value: "02138"
```

In 99% of cases this is what we want. Except that now there's a catch. The `.withRecursiveComparison()` does NOT use your object's `.equals()` method! So now we're back to:

```bash
field/property 'created' differ:
- actual value  : 2026-07-13T14:09:09.060220Z
- expected value: null
```

Since in this case, our model doesn't get a `created` timestamp until after it's inserted into the db, we'll never be able to have expected `created` equal `actual` created.

Thankfully, we have at our disposal `.ignoringFields()` and `.ignoringFieldsOfType()`. For this object, with timestamps that we know will never be equal, it makes the most sense to do:

```java
assertThat(actual)
.withRecursiveComparison()
.ignoringFieldsOfType(Instant.class)
.isEqualTo(expected);
```

This, as you'd expect, causes the comparator to skip all fields of type Instant.

But wait. What if there's also an auto-incremented database id that we want to ignore?

```java
assertThat(actual)
.withRecursiveComparison()
.ignoringFieldsOfType(Instant.class)
.ignoringFields("id")
.isEqualTo(expected);
```

Instead of specifying which fields to ignore, we could also specify which fields we want to compare, with `comparingOnlyFields(String)` or `comparingOnlyFieldsofType(Class<?>)`, although if I were in that situation I would probably see myself instead using the `.extracting` method, like so:

```java
assertThat(actual).extracting("name","age").containsExactly("John Doe",32);
```

But back to recursive comparison! We can also add on `.ignoringCollectionOrder()` which will compare the contents of two lists, without worrying about the order in which elements appear, or register a custom comparator for a specific field. For the latter, I can't really write a better example than the [official AssertJ one](https://javadoc.io/doc/org.assertj/assertj-core/3.17.2/org/assertj/core/api/RecursiveComparisonAssert.html#withEqualsForType(java.util.function.BiPredicate,java.lang.Class)), so see:

```java
public class TolkienCharacter {
   String name;
   double height;
 }

 TolkienCharacter frodo = new TolkienCharacter("Frodo", 1.2);
 TolkienCharacter tallerFrodo = new TolkienCharacter("Frodo", 1.3);
 TolkienCharacter reallyTallFrodo = new TolkienCharacter("Frodo", 1.9);

 BiPredicate<Double, Double> closeEnough = (d1, d2) -> Math.abs(d1 - d2) <= 0.5;

 // assertion succeeds
 assertThat(frodo).usingRecursiveComparison()
                  .withEqualsForType(closeEnough, Double.class)
                  .isEqualTo(tallerFrodo);

 // assertion fails
 assertThat(frodo).usingRecursiveComparison()
                  .withEqualsForType(closeEnough, Double.class)
                  .isEqualTo(reallyTallFrodo);
```

This custom comparator could also be used to prove that the height of Treebeard+Merry is equal to the height of Treebeard alone. In case you ever needed to do that.

This is hopefully all you[^1] ever needed to know about deep object equality testing!

[^1]: I. It's all *I* needed to know.
