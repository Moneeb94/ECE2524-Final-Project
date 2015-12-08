#Snake game
# To play the snake game, use the arrow keys to move
# If you run into the wall or a part of the snakes 
# body, the game is over

import curses
import random
from curses import KEY_LEFT, KEY_DOWN, KEY_UP, KEY_RIGHT
from random import randint

curses.initscr()
win = curses.newwin(30, 70, 0, 0) 
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

#Initialize the snake to move left when the game first starts
key = KEY_LEFT

#Intitial starting position of the snake
snake = [[5,10], [5,9], [5,8]]

#Initial Food Co-Ordiniate position
food = [10,20]

#add food to the screen
win.addch(food[0], food[1], '*')

while key != 27:
  win.border(0)
  
  #Prints the score while you are playing the game
  win.addstr(0, 10, 'SCORE: ' + str(score) + ' ')
  
  #Prints the snake's head and body while you are playing the game

  




