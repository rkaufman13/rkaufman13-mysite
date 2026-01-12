---
layout: post
title: "Works In Progress: Generating a Maze in Python"
categories: things-i-learned
excerpt_separator: <!--more-->
description: And some random game dev thoughts.
image: /assets/maze.jpg
---

![A photo, possibly AI-generated? of a circular hedge maze. Maybe it's not AI generated. It looks sus is all.](/assets/maze.jpg)

Last year I was messing around with maze generation. I thought I was going to make another game (more on that later). I didn't get very far, but I did learn how to use the recursive backtracking algorithm to create a 2D maze. I was thinking about that algorithm again during Advent of Code, as many of the problems turn out to be maze/traversal problems, and, well, I've been meaning to write this up anyway. It's not really a complete project, but I found it interesting, and maybe you will as well?

There are a lot of [maze algorithms](https://www.astrolog.org/labyrnth/algrithm.htm) out there. The recursive backtracking one is one of the easiest, I'm told.

The general gist: Start with a grid of possible spaces. Choose one to start, and "knock down" the wall between it and a random neighbor. Choose another direction at random, and if it has not yet been visited, knock down the wall there. Once all locations at a given square have been visited, backtrack; once the algorithm reaches the starting point the maze is complete.

Implementing it in Python looks like this:

```python
DX={"N":0,"S":0,"E":1,"W":-1}
DY={"N":-1,"S":1,"E":0,"W":0} 

class Maze():
    def __init__(self, size, seed="default"):
        #init the maze
        self.size = size
        self.game_map=np.zeros(shape=(self.size,self.size),dtype=object)
        for y,row in enumerate(self.game_map):
            for x, square in enumerate(row):
                self.game_map[y][x] = Room(x, y) #this is not strictly necessary, I wanted my maze Room class to have some other features that I will discuss later
        start_x = random.randint(0,self.size-1)
        start_y = random.randint(0,self.size-1)
        self.make_the_maze(start_x,start_y)

    def make_the_maze(x,y):
        current_room=self.get_room(x,y) #returns an instance of the Room class with these xy coordinates
        current_room.visited=True
        directions = ["N","S","E","W"]
        random.shuffle(directions)
        for direction in directions:
            new_x = x+DX[direction]
            new_y = y+DY[direction]
            if (0<=new_y and new_y<self.size) and (0<=new_x and new_x<self.size) and not self.get_room(new_x,new_y).visited:
                #recurse
                self.make_the_maze(new_x,new_y)

maze = Maze(3)
```

This allows us to declare a square maze of length and width `n` and create a maze where all squares are visited at least once and with one entry and exit. This implementation doesn't really *do* anything, though -- ideally we would be, oh, counting the number of valid, unique paths from point A to point B, for example. Or rendering it on a screen.

![Three mini-mazes](/assets/mini-mazes.png)

What I wanted to do with *this* maze, though, is turn it into a text adventure. By saving each room's doors (e.g. `doors: {'N':True,'S':False}` etc...) I can use that to generate an Inky file:


```python
    #still in the Maze class
    def render_text(self, start_x, start_y):
        with open("game.ink","w+") as inkfile:
            inkfile.write("You are about to enter the spooky maze!\n")
            inkfile.write(f"+[Go in] -> room_{start_x}_{start_y}\n")
            for room in self.get_all_rooms():
                self.write_room(inkfile, room)
    def write_room(self, inkfile, room):
        x = room.x
        y = room.y
        inkfile.write(f"===room_{x}_{y}===\n")
        if room.is_finish:
            inkfile.write("You have found the exit and/or the amazing treasure!->END")
        else:
            inkfile.write("You are standing in a maze of twisty passages, all alike.\n")
            doors = room.get_doors()
            exits = [direction for direction in doors if doors[direction]]

            if len(exits)>1:
                inkfile.write(f"There are exits to the {','.join(exits)}\n")
            else:
                inkfile.write(f"There is an exit to the {exits[0]}.\n")
            for door in exits:
                new_x = x+DX[door]
                new_y = y+DY[door]
                inkfile.write(f"+[Go {door}] -> room_{new_x}_{new_y}\n")
```

An `.ink` file is used by the [Inky editor](https://www.inklestudios.com/ink/) to create narrative adventures. The Inky editor uses a Markdown-ish syntax to create choose-your-own-adventure style games.

I had this idea that I could make a procedurally-generated choose-your-own-adventure (with more interesting narration than the "maze of twisty passages" stuff, of course) and then, using the same seed, create a visual representation of the same maze, that two players would solve together. The `Room` class would be essential for this and would contain things like: does this room contain a locked door, or a key, or a monster, or a landmark? I haven't gotten around to implementing it yet but you get the general idea.

So, it's pretty bare-bones and doesn't do anything yet, but to my knowledge (and upheld by a very quick Google--please reach out if I missed you) this is one of the earliest examples of procedurally generated Inky games. I hope to have some time to get back to this eventually, but *\*waves hands\** life has been getting in the way. For now, I'm happy to have had a chance to learn a maze algo.

### Resources ###

I am indebted to Jamis Buck's 'Buckblog' post on maze generation; his [writeup in Ruby](https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking) was the only thing that helped me make sense of doing the same in Python. It should be noted that he has [an entire book](https://pragprog.com/titles/jbmaze/mazes-for-programmers/) about mazes that I am probably going to be buying shortly.
