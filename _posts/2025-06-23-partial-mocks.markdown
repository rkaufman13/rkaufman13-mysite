---
layout: post
title: Partially Mocking a Class in Java
categories: things-i-learned
excerpt_separator: <!--more-->
description: This will save a lot of time.
image: /assets/nelson.png
---

![Nelson from the Simpsons pointing and saying "HA-HA!".](/assets/nelson.png)
*This is an example of complete mocking, but not the kind of mocking this post discusses.*

I love writing unit tests. i know this is an unpopular opinion but I just really like it. I love thinking of edge cases that could break code and then coming up with exactly how to create a test that will prevent that.

However, mocking everything stinks. Yes, we should be using in-memory fakes instead of mocks as much as possible, and I've been working toward this, but it is not realistic to make *everything* a fake.

My very smart coworker just alerted me to this method built into Mockito's `when` method, which is used for controlling the behavior of mocks. If you want to stop reading now, just read the next two lines, and then you can go:

`when(thing.method()).thenCallRealMethod()`

This bypasses any mock behavior and goes back to the real class's implementation. Handy!

For absolutely more details than you need, here's an example:

```java
class MyClass(){
 public int myMethod(){
  return 1;
 }
}

class SomeTestClass(){
 public MyClass myClass = mock(MyClass.class);

 int result = myClass.myMethod();

 assertEquals(1, result);
}
```

This contrived example will fail, because we haven't explicitly declared the behavior of `myMethod`. (It will return `null` instead.)

So what I would have done yesterday would look like this:

```java
class MyClass(){
 public int myMethod(){
  return 1;
 }
}

class SomeTestClass(){
 public MyClass myClass = mock(MyClass.class);
 when(myClass.myMethod()).thenReturn(1);
 int result = myClass.myMethod();

 assertEquals(1, result);
}
```

This will work (ignore the part where this test is a tautology!), but if your method under test has a lot of external calls that you're mocking out, this can get messy. That's where `.thenCallRealMethod()` comes in. If you had:

```java
class MyClass(){
 public int myMethod(){
  return 1;
 }
 public int someOtherMethod(){
  return 3;
 }
}

class SomeTestClass(){
 public MyClass myClass = mock(MyClass.class);
 when(myClass.myMethod()).thenReturn(2);
 when(myClass.someOtherMethod()).thenCallRealMethod();
 int result = myClass.myMethod();
 int result2 = myClass.SomeOtherMethod();

 assertEquals(2, result); //true because we have mocked the behavior of this method
 assertEquals(3, result2); //true because the real method returns 3
}
```

Like I said: Handy!
