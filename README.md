# ⚔️ Adventure game
## A. Project Overview

In this project, you'll make a simpler version of an old-fashioned text-based adventure game. You can find an example in the workspace below. Try it out to get a feeling for how the game works!

In order to build a program like this, we should first completely understand what it does. Take a notepad out, and play the game multiple times. The game will present you some scenarios and ask you to make one of 2 choices, by entering 1 or 2. In your notepad, record what happens each time you make a certain choice.

    Note: Before doing this project, be sure to have completed the Style and Structure lesson in Intro to Python, Part 2.

As you can see, this is only a very short game with a couple of choices available to the player. We did that on purpose, to keep it simple. If we were making a complete game, we would expand it a great deal, and probably give the player a whole world to explore. But for this project, the idea is to focus on some key things that we need if want to make a working game:

    The game gives players a description of what's happening, and then asks them to make a choice.
    Something different happens depending on the choice the player made.
    The game also includes some random factors, so that it's a little different each time.
    The game has conditions for winning and losing.
    When the game is over, it asks if the player wants to play again.

These are the key features that your project will need to have in order to make it into a playable game. We'll go over each of them in more detail below.

As long as your program does all of the things listed in the instructions below, you are free to be as creative as you like!
Workspace or Local Environment

We've provided a workspace that you can use to complete this project (see the page titled Project Workspace. We suggest that you open these instructions in a second tab or window so you can have them alongside the workspace as you write your code.

If you prefer, you can also write your code on your own machine and copy it into the workspace when you're ready to submit.
B. Project Rubric

When doing a Udacity Project, it's an excellent habit to view the rubric once before doing the project (to understand the requirements) and once after doing the project (to check your work). You can go to the Project Rubric page to read the details. For your convenience, the next page also describes the rubric.
C. Project Instructions

## 1. Print descriptions of what's happening for the player

One thing the game will need to do is to print messages for the player to describe what is happening. Like at the start of the example game, these lines are printed:

You find yourself standing in an open field, filled with grass and yellow wildflowers.  
Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.

## 2. Pausing between printing descriptions

Now, one thing you might have noticed is that when you have multiple print statements, they get displayed in the terminal so fast that it looks like they all just show up at the same time. That's no good.

If you look at the example game, there's a short delay after each line is printed.

You may remember that earlier in the course, we briefly introduced the time module and the time.sleep() function:

import time
print("Hello")
time.sleep(2)
print("world!")

...
## 3. Give the player some choices

Up till now, our program prints the introduction of the game, with short pauses in between each sentence. Another important element of any good adventure game is choice. To do this, you'll need to get some input from the player, and then change what happens depending on what that input is. In the example game, that looked like:

Enter 1 to knock on the door of the house.  
Enter 2 to peer into the cave.  
What would you like to do?  
(Please enter 1 or 2).  

In the example game, each time we make a choice, something happens, and we are offered 2 choices again till we win or lose. For now, just focus on writing code for the 2 choices you have.

    If the player knocks on the door of the house, what happens?
    If the player enters the cave, what happens?

We will be dealing with subsequent choices after the first choice in the upcoming steps.

## 4. Make sure the player gives a valid input

Up till now, our program prints a description of the game-world to the player, gives them a choice, and prints what happens depending on their choice. An important thing to notice in the example game is that if the player enters something other than 1 or 2, the game keeps asking them for a 1 or 2. We don't want the game to accept invalid input, like 75 or foo!

(Please enter 1 or 2.)
75
(Please enter 1 or 2.)
foo
(Please enter 1 or 2.)

If the player tries to respond with something invalid, your program should ask them to try again—and it should keep asking them to try again until they give valid input.

Recall the data type in which the input() functions stores the user input, and add code accordingly.

## 5. Add functions and refactor your code

By now, you may have noticed that some of your code is getting pretty messy, and some parts may be kind of repetitive. If you haven't already, this would be a good time to consider defining some functions, and moving some of your code into those functions.

For example, you probably have a lot of code that looks like this:

print("You find yourself standing in an open field, filled with grass and",
      "yellow wildflowers.")
time.sleep(2)
print("Rumor has it that a wicked fairie is somewhere around here, and has",
      "been terrifying the nearby village.")
time.sleep(2)
print("In front of you is a house.")
time.sleep(2)
print("To your right is a dark cave.")
time.sleep(2)
print("In your hand you hold your trusty (but not very effective) dagger.")
time.sleep(2)
....

This is quite repetitive—we are using print, sleep, print, sleep, print, sleep, over and over ...

One improvement that you can make is to define your own function so that it will both print and sleep—you might call it the print_pause function.

With such a function, you could simply pass it a message to print, and it would take care of the pausing:

print_pause("You find yourself standing in an open field, filled with grass",
            "and yellow wildflowers.")
print_pause("Rumor has it that a wicked fairie is somewhere around here,",
            "and has been terrifying the nearby village.")
print_pause("In front of you is a house.")
print_pause("To your right is a dark cave.")
print_pause("In your hand you hold your trusty (but not very effective)",
            "dagger.")
....

Here's another way you can use functions in a game like this—you can define a function for each place the player can go. In the example game, the code looks something like this:

def fight():
    # Things that happen when the player fights  

def cave():
    # Things that happen to the player goes in the cave  

def field():
    # Things that happen when the player runs back to the field

def house():
    # Things that happen to the player in the house

That way, when the player chooses to go to one of these places, you can simply call the function that displays the description and choices for that place. This is especially good if you want the player to be able to go back to the same place repeatedly, from different locations in the code. In the example game, the player can get back to the field from both the house and the cave, and having the field function makes this much easier.

Usually, each function will print what happens after the player takes a certain choice, then offer another choice, and call the specific function depending on the choice the player makes. In the end, you would want to have a play_game() or main() function, which starts the game.

These are just a few examples of how you can use functions in your project. You'll probably find other ways you can clean up the code and reduce repetitiveness by defining (and calling) functions. (In fact, it's possible to do this project with almost every line of code being placed inside a function definition!)

