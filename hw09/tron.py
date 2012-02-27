#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

#FYI:
#This is here because you asked me to put it here so you wouldn't have to remember.
#I worked with Nathan, which is why our codes may seem similar. Very similar.

import pygame
from pygame import draw
from pygame.locals import *

orange = (234,144,0)
blue = (0,243,213)

north = (0, -1)
east = (1, 0)
west = (-1, 0)
south = (0, 1)

tile = 10
width = 80
height = 60

#player directions @start. 
direct1 = east
direct2 = west

pos1 = [(10, 10)]
pos2 = [(70, 50)]

#This may or may not be necessary in the future. Woo, future.
#Edit: it's not. I'm not using a function to define the players. Muahahaha. I'll leave this in here for nostalgia, just because. Mmm ... nostalgia. 
"""
def draw_players(pos1,pos2):
    p1x,p1y = pos1
    p2x,p2y = pos2
    pygame.draw.rect(screen,orange,(p1x,p1y,10,10))
    pygame.draw.rect(screen,blue,(p2x,p2y,10,10))
"""

def move_player(pos, direct):
    newPos = (pos[0] + direct[0], pos[1] + direct[1])
    return newPos

def collision(next_pos, pos1, pos2):
    x,y = next_pos

    if x >= width or x < 0 or y >= height or y < 0:
        return True
    elif next_pos is pos1:
        return True
    elif next_pos in pos2:
        return True
    else:
        return False

pygame.init()

screen = pygame.display.set_mode((width * tile, height * tile)) #IT'S THE GRID

done = False
playing = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE:
            playing = True

        #player 1
        elif event.type == KEYDOWN and event.key == K_w and direct1 !=south:
            direct = north
        elif event.type == KEYDOWN and event.key == K_a and direct1 !=east:
            direct1 = west
        elif event.type == KEYDOWN and event.key == K_s and direct1 !=north:
            direct1 = south
        elif event.type == KEYDOWN and event.key == K_d and direct1 !=west:
            direct = east

        #PLAYER 2!
        elif event.type == KEYDOWN and event.key == K_UP and direct1 !=south:
            direct2 = north
        elif event.type == KEYDOWN and event.key == K_LEFT and direct1 !=east:
            direct2 = west
        elif event.type == KEYDOWN and event.key == K_DOWN and direct1 !=north:
            direct2 = south
        elif event.type == KEYDOWN and event.key == K_RIGHT and direct1 !=west:
            direct2 = east

        #update ALL the players!
    if playing:
       next_pos1 = move_player(pos1[-1], direct1)
       next_pos2 = move_player(pos2[-1], direct2)

       collision1 = collision(next_pos1, pos1, pos2)
       collision2 = collision(next_pos2, pos1, pos2)

       if collision1 or collision2:
            playing = False
            if collision1 and collision2:
                print "Both lose"
            elif collision1:
                print "player 2 wins"
            else:
                print "player 1 wins"
       else:
           pos1.append(next_pos1)
           pos2.append(next_pos2)

    #draw ALL the players
    screen.fill((5,5,5))
    for x,y in pos1:
        pygame.draw.rect(screen, orange, (x*tile,y*tile, tile, tile))
    for x,y in pos2:
        pygame.draw.rect(screen, blue, (x*tile, y*tile, tile, tile))

    #Do that shit.
    pygame.display.flip()
    clock.tick(30)
        

print "running away, are we?"
