---
layout: post
title: Why I'm Not Doing Advent of Code (in Go)
categories: musings
excerpt_separator: <!--more-->
description: Even though that mascot is *chefs kiss*
image: /assets/go_mascot.png
---

![A cute 3d printed version of the Go mascot](/assets/go_mascot.png)

I want to learn Go.

- another statically typed language would be good to have under my belt
- everyone seems to LOVE go
- I want to see what all the fuss is about and stretch my brain

Ergo[^1], I should do a bunch of coding puzzles this month in go, right?

That's what I thought, until I actually started working with go. Perhaps embarrassingly, I didn't know much about go before that other than the facts listed above: it's strongly typed, and developers who use it love it, like Crossfit cult levels of love. Obviously I want to know what all that is about.

After I went through a few tutorials, I decided that I like:

- My god it's fast. Go says "you won't feel like you're running a compiled language" and that is absolutely true.
- Go's error handling feels a lot like the `Either` control structure in Java that we use a lot at work, so while I don't have strong opinions on whether that's the "best" way to do error handling, at least it's familiar
- Pointers (jk, I do not like these, but I should probably learn how to use them eventually)

However, besides those strengths, Go is not the best language for me for Advent of Code, which (in my experience) requires being fast, flexible, and a little bit hacky. This is the canonical way to reverse a string in go:

```golang
func reverse(s string) string {
    chars := []rune(s)
    for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
        chars[i], chars[j] = chars[j], chars[i]
    }
    return string(chars)
}
```

In hindsight, Go's strengths are not those that serve one person doing silly coding puzzles for a month[^2]. As I have now read, Go is fabulous for concurrency, memory management, for working on big codebases with multiple people, and for [deploying across multiple computers](https://hackernoon.com/the-beauty-of-go-98057e3f0a7d), none of which I will be doing in December.

The other factor that worried me is that Advent of Code prioritizes speed. Not that I'm going to be hitting any leaderboards, but I still want to keep up with the daily exercises. I got to worrying that learning a new language while trying to be that fast might start me off learning bad patterns, and I want to learn Go correctly.

So for Advent of Code this year, it's back to Python for me, which is great because I can always improve there too. [The first day wasn't so bad so far.](https://github.com/rkaufman13/advent-of-code-2024) And I've picked out a [Coursera course on Go](https://www.coursera.org/specializations/google-golang#courses) that I'll be working through instead.

[^1]: hee hee :)

[^2]: or in my case, the first two weeks.
