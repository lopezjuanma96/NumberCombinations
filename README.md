# Game of Number Combinations

## Motivation
This codes emulate a card game I've learned a few years ago.
The original card game consists of flipping 5 cards, 4 in the center and one on the side.
Each card represents it's numerical value, though it's convenient to work with numbers ranging 1-10.
Ones the cards are flipped, players start trying to figure out how to combine the values of the 4 cards in the center to get the value of the card aside as a result, with basic operations (I believe there could be a way to work it out with powers and roots, but upto now it's just +, -, x, /).
When each player knows the answer (or lies about knowing it) they knock the table, until only one remains: that person has to decide who of the others (who supposedly knew the answer since they knocked the table) gives the result. If the answer is correct, then that last person gets a -1, if the answer is incorrect or the chosen one doesn't not know it's them who get the -1.
There are two posible ways for the game to run:
- Everyone plays all the time, until one gets to a certain value when they lose, and everyone else win.
- When someone gets a -1 (or gets to a certain value) they get eliminated and the game continues until only one player is left. That person is the winner.

##Adaptation
This code emulates that game by giving a random or chosen set of x amount of numbers as operands and a result, and after confirmation gives all the possible answer. I'm working on improving it and adding a Visual Interface (maybe with flipping cards?). It's a project I do in my free time so don't expect too quick of a progress. It also helos me learn new techniques for Python.

## Possible Variations
I thought of some possible variations of the game:

- As said before, maybe powers and roots could be added as operations too, but also concatenation (if you have 1 and 9 you can get 19). Should work out first how to implement them so that the rules are fair and the game does not become too easy.
- Add a timer, so that more than one person can end the round without knocking. Should think of what to do when that happens.
- Add a rule (random or cyclical) for some of the operations being unavailable some of the rounds, or some of the cards being flipped down until a player has to give the answer (or maybe there could be an extra flipped down card that the player who has to say the answer CAN flip if they don't know what the answer is and that might help them or not).

If you can think of other variations share them in Issues.

## Up to Now
The code can generate a set of x amount of random numbers as operands and another random number as a result, or let you select the set that you'd like to use.
This are generated through a Class called GameParams()
Some other functions that might be useful for other projects include "all_permutations" that gives all the permutations that an array can be found in, and "all combinations" that gives all the possible combinations of the elements of an array onto another array of the same or different size.

## To-Do List
Add more details commentaries and descriptions for Classes and Functions.
Add Player Class. -> this class will have a class variable that keeps the amount of players created and how many of them haven't "knocked" on each round.
Add a Visual Interface. -> Try Dear PyGUI, Tkinter or Processing.
Create Executable. -> C?

