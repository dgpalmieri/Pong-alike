# Order of happening things in a game of Pong:
1. Ball is served in a random direction
2. Ball bounces off wall
3. Player hits ball
4. Ball hits other player's wall, scoring a point

# Requirements to play a game:
Ball

Paddles

Walls

Scoreboard

# Mechanics
Ball bounces off walls and paddles

Gain points when ball hits player's walls

Players' paddles move

# Organization

### Global Variables

Up

Neutral

Down

### Block class - base class

abstract Paddle class - contains movement methods
		
abstract Wall class
	
### Ball class

collision method
	
scored - returns true if scored
	
whoScored - returns the number of the player who scored
	
### Scoreboard class

ifScored - maintains score, querys ball.scored and updates board

# Blocking

Start game

"First to 10 points is the winner! /n Press Spacebar to serve, escape to quit first to 10 points wins" - paddles can move before serve
ball is served in a direction +- 45degrees from midline from the middle of the board 
Continue until 10 pts or until escape is pressed
