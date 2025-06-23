---
layout: post
title: "Don't Sync State, Derive It! (With Apologies to Kent C. Dodds)"
categories: things-i-learned
excerpt_separator: <!--more-->
project: "Bookguessr"
description: Learning a years-old lesson. Again.
image: /assets/synchronized_swimming.jpg
---

![An image of synchronized swimmers doing their thing.](/assets/synchronized_swimming.jpg)
*Syncing is for swimming, not for state.*

This is a pretty standard lesson (Kent C. Dodds talks about it a lot in his React courses and [on his blog](https://kentcdodds.com/blog/dont-sync-state-derive-it)) but it's still something that has taken me a while to internalize.

With BookGuessr, I have a bunch of state!

I have the list of all books that could possibly be part of the game, the list of books that is part of the current game, the score, the high score, the game's status (started or ended), and probably some other stuff. This is a lot to keep track of, and despite knowing what I know, my first draft of the app looked like this:

```js
const [allBooks,setAllBooks]= useState(initialListOfBooks);
const [chosenBooks,setChosenBooks] = useState([]);
const [score, setScore] = useState(0);
const [gameIsActive,setGameIsActive] = useState(false);
...
```

and so on. Easy to write, not so easy to track.

Now, if a player chooses a book, we need to:

- remove that book from the list of available books
- add that book to the list of chosen books
- check if the score needs to increase, and increase it if so
- check if the game needs to end, and end it if so

That's four separate state variables we need to manage! But we really only need to manage one state, if we turn our `allBooks` variable into something like this:

```js
[{'title': 'The Grapes of Wrath','author':'John Steinbeck','year':1939,'correct':true},{'title': 'Middlemarch','author':'George Eliot','year':1871},{'title': 'Snow Crash','author':'Neal Stephenson','year':1992,'correct':false}...]
```

There are probably lots of ways to slice this, but this is the structure I have decided on (for now). Now, `score` is calculated by performing `allBooks.filter(book=>book.correct).length`, `chosenBooks` are calculated by filtering on the same condition and sorting by year, `gameIsActive` can be calculated by finding if any item in the array has the `incorrect` key, and so on.

This turns the above code into something more like:

```js
const [allBooksForGame, setAllBooksForGame] = useState(allBooksWithDates());

const currentBook = chooseNextBook(allBooksForGame);

const score = calculateScore(allBooksForGame);

const highScore = calculateHighScore(score);
```

This is pretty clean (the implementations of the helper functions I'll leave up to the reader), but more importantly, when `allBooksForGame` changes, everything else updates without the programmer having to do anything.
