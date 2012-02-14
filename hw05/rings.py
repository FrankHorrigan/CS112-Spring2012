#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255
OFFWHITE = 250,250,250

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")


#################################
##  DRAW OLYPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################

#I have no idea what I'm doing.

## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    ##Draw
    screen.fill(OFFWHITE)
#Hee hee hee. colors. trololololol.
    pygame.draw.arc(screen,BLUE,(40,15,230,230),20,179,22)
    pygame.draw.arc(screen,BLACK,(290,15,230,230),20,179,22)
    pygame.draw.arc(screen,RED,(540,15,230,230),20,179,22)
    pygame.draw.arc(screen,YELLOW,(165,135,230,230),20,179,22)
    pygame.draw.arc(screen,GREEN,(415,135,230,230),20,179,22)
    pygame.display.flip()
    clock.tick(30)

print "Find Vic in Klamath."
