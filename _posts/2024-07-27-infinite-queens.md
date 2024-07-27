---
layout: post
title: "Building a Queens clone in React"
categories: stuff-i-made
excerpt_separator: <!--more-->
---

![This is a queen, right? I'm actually terrible at chess](assets/queens-header.jpg)

I have nearly a 50-day streak on [Queens](https://www.linkedin.com/showcase/queens-game/), a daily game from [the worst social network](https://www.linkedin.com). The fact that LinkedIn has managed to trick me into visiting daily is not lost on me, but man, it's a fun game.

I decided that one Queens per day is not enough, and so I've built [Infinite Queens](https://rkaufman13.github.io/infinite-queens/). The original Queens puzzle, which Infinite Queens is based on, is fairly simple: place eight queens on the chessboard such that no two queens could capture each other. That means no queens in the same horizontal, vertical or diagonal line. LinkedIn's Queens actually is more complex and, I think, more interesting, but I started with the easier problem: How can I make a puzzle that replicates the O.G. Queens, but is different every time you refresh the page?

Because there are [only 96 solutions to Queens](https://users.encs.concordia.ca/~chvatal/8queens.html), and the majority of them are created by transforming other solutions, I decided that the solutions can be hardcoded. Basically, create hardcoded 2D arrays with the solutions, and at game time, we can choose one at random, then flip or rotate the array to create an alternate game board, then remove all but 2-3 of the starting pieces to give the player something to start with.

At that point, I'm honestly not sure whether the puzzle is "well-formed" -- meaning, whether there is only one solution to the given configuration. I suspect there is more than one solution, so the game only checks whether the board is valid, not whether it matches the original configuration.

I started with one board:

<!--more-->

```js
const solution = [
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0],
];
```

and wrote code to confirm the board was valid, which it is. Perfect!

I went on to design some simple React components (imagine the tic-tac-toe tutorial and you're basically there) and wire up a quick UI that allows the user to click a square to toggle between "queen" and "no queen." On every click, the app should check the state of the board and display a "you win" message if the board is a valid solution.

 I grabbed my `isBoardValid` function and wired it into the state of the board and ...

<img src="/assets/invalid1.png" alt="not actually a valid board" class="post"/>

...got a 'You Win' message here.

..Hey, wait a minute...

<img src="/assets/invalid2.png" alt="DEFINITELY not an invalid board" class="post"/>

This one also told me I won. Excellent reminder for me: always test your tests. :)

Once I got that straightened out, my next step was to bring in the other 12 'base' boards to add more randomization to the starting configurations. As mentioned, there are only 96 solutions to Queens, and all of them are created from 12 'base' solutions, either rotating or flipping them. So all I have to do is make 11 more arrays like the one above...I'm already bored.

Wouldn't it be nice if there was an easier way? After a nice shower to clear my head, I realized there was. Each valid board can actually be represented as a 1D array. In this case, the index represents the row, and the value at that index represents the column. For example, the board above can be represented as:

```js
const solution = [0,4,7,5,2,6,1,3]
```

We can turn that into a board with the following code:

```js
 const randomIndex = Math.floor(Math.random() * 11); //we have 12 possible solutions to choose from in a 0-indexed array
  const solution = solutions[randomIndex]; //get one random solution from the list of possible solutions

//create an 8x8 2D array filled with zeroes
  let matrix = Array.from({ length: 8 }, () =>
    Array.from({ length: 8 }, () => 0)
  );
  
  //put the queens in the correct place
  for (let i = 0; i < 8; i++) {
    matrix[i][solution[i]] = 1;
  }

```

We could actually check the solution by converting it back to a 1D array. I believe that any array of length 8, that contains no duplicates or consecutive values, would be a valid solution. However, my 2D validity checker is working fine, and if it ain't broke I won't fix it. ;)

From there, as mentioned, I just have to randomize the board by rotating or flipping it, and then remove most of the starter queens. That way we are guaranteed to have a game that is solvable, but different from any other starting position.

Now our base game is ready. We have a way of generating valid boards and a way to test whether a user's submission is valid. At this point, the only thing that remains is to clean up the React components and publish.

I used the `gh-pages` npm package to publish the build to Github Pages in one line, following [this](https://blog.logrocket.com/deploying-react-apps-github-pages/) tutorial. I'm pleased at how easy this is and will absolutely be publishing future static sites this way.

 The question remains: is it _fun_? I'll let you be the judge of that.

Play [Infinite Queens](https://rkaufman13.github.io/infinite-queens/) on github.io today.
