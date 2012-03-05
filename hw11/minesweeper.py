#!/usr/bin/env python

from random import randrange

import pygame
from pygame.locals import *

##settings
FPS = 30


#colors
C_BORDER = 15,15,15
C_HIDDEN = 120,120,120
C_ACTIVE = 255,255,255
C_HOVER = 175,175,175
C_CLEARED = 200,200,200
C_BOMB = 0,0,0
C_FLAG = 245,23,23

def clear_square(world,x,y):
    world[x][y]["cleared"] = True
    return world[x][y]["bomb"]

def flag_square(world,x,y):
    world[x][y]["flagged"] = not world[x][y]["flagged"]


# Game
def game(tile, width, height, num_bombs):
    #init
    screen = pygame.display.set_mode((width*tile, height*tile))
    num_flag = num_bombs

    world = []
    for x in range(width):
        row = []
        for y in range(height):
            cell = {}
            cell["bomb"] = False
            cell["rect"] = pygame.Rect(x*tile, y*tile, tile, tile)
            cell["cleared"] = False
            cell["flagged"] = False
            row.append(cell)
        world.append(row)

    #PLACE THE BOMBS
    c = 0
    while c < num_bombs:
        x = randrange(width)
        y = randrange(height)
        if not world[x][y]["bomb"]:
            world[x][y]["bomb"] = True
            c += 1
        #if not already bomb
            #make bomb
    



    ##Flags
    lmb_clicked = False
    rmb_clicked = False
    action_clear_square = False
    action_flag_square = False
    gameover = False

    #loop
    clock = pygame.time.Clock()
    done = False
    while not done:
        #input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True

            #Maus
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                lmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                lmb_clicked = False
                action_clear_square = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                rmb_clicked = True
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                action_flag_square = True
                rmb_clicked = False


        #update
        if action_clear_square:
            x,y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            if not world[x][y]["flagged"]:
                gameover = clear_square(world, x, y)
            action_clear_square = False

        if action_flag_square:
            x,y = pygame.mouse.get_pos()
            x /= tile
            y /= tile
            if num_flag > 0 and not world[x][y]["flagged"]:
                world[x][y]["flagged"] = True
                num_flag -=1
            elif world[x][y]["flagged"]:
                world[x][y]["flagged"] = False
                num_flag +=1
            
            action_flag_square = False


        if gameover:
            for x in range(width):
                for y in range(height):
                    world[x][y]["cleared"] = True

        #display
        screen.fill(C_BORDER)
        for x in range(width):
            for y in range(height):
                rect = world[x][y]["rect"]

                #cell color
                if world[x][y]["cleared"]:
                    bg_color = C_CLEARED
                elif lmb_clicked and rect.collidepoint(pygame.mouse.get_pos()):
                    bg_color = C_ACTIVE
                elif rect.collidepoint(pygame.mouse.get_pos()):
                    bg_color = C_HOVER
                else:
                    bg_color = C_HIDDEN
                
                #draw background
                screen.fill(bg_color, rect.inflate(-3, -3))

                if world[x][y]["cleared"]:
                    if world[x][y]["bomb"]:
                        pygame.draw.ellipse(screen, C_BOMB, rect.inflate(-20, -20))
                        pygame.draw.rect(screen, C_BOMB, rect.inflate(-25,-25))
                        
                    
                if not world[x][y]["cleared"]:
                    if world[x][y]["flagged"]:
                        pygame.draw.rect(screen, C_FLAG, rect.inflate(-25,-25))
                

                        

                    


        #refresh
        pygame.display.flip()
        clock.tick(FPS)

#application
def main():
    pygame.init()
    game(50, 10, 10, 10)

main()
print "Running away, are we?"
