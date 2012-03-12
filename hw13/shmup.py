#!/usr/bin/env python

#IT'S INCOMPLETE. I'm turning in what I managed to finish, and I'll turn it in again when I've finished it.

#My name is Piper Odegard.

#Shmup. 

import pygame
from pygame import Rect, Surface
from pygame.locals import *

from app import Application

FPS = 30
Clock = pygame.time.Clock()

#pygame.sprite.Sprite()
#x = pygame.sprite.Sprite()


class Player(pygame.sprite.Sprite):
    width = 40
    height = 60
    x = 380
    y = 740

    def __init__(self, x, y, vx, vy, bounds):
        pygame.sprite.Sprite.__init__(self)

        self.vx = 0
        self.vy = 0
        self.bounds = bounds
        self.color = (255,0,0)

        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw()


    def draw(self):
        self.image.fill(self.color)

    def update(self, dt):
        dt /=1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)

        self.rect.x += dx
        self.rect.y += dy
#BOUND LEFT
        if self.rect.left < self.bounds.left:
            self.vx = 0
            self.rect.left = self.bounds.left
#BOUND TOP
        if self.rect.top < self.bounds.top:
            self.vy = 0
            self.rect.top = self.bounds.top
#BOUNDS RIGHT
        if self.rect.right > self.bounds.right:
            self.vx = 0
            self.rect.right = self.bounds.right
#BOUNDS BOTTOM
        if self.rect.bottom > self.bounds.bottom:
            self.vy = 0
            self.rect.bottom = self.bounds.bottom


#I HAVE YET TO MEET CLASS BULLETS.
class Bullet(pygame.sprite.Group):
    width = 8
    height = 16
    
    def __init__(self, Bullet, vy):
        pygame.sprite.Sprite.__init__(self)
        self.vy = 1000
        self.bounds = bounds
        self.color = (255,255,255)

        self.rect = Rect(player.rect.midtop, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw()


    def draw(self):
        self.image.fill(self.color)

    def update(self, dt):
        dt /=1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)

        self.rect.y += dy
 
        
        


##THE GAME
class Game(Application):
    title = "Piper's Shmup"
    screen_size = 800, 800
    min_dt = 200

    done = False
    playing = False
    clock = pygame.time.Clock()

    def __init__(self):
        Application.__init__(self)
        self.bounds = self.screen.get_rect()
        self.player = Player(380, 740, 6, 6, self.bounds)

    def handle_event(self, event):
#MOVING UP
        if event.type == KEYDOWN and event.key == K_w:
            self.player.vy = -300
        elif event.type == KEYUP and event.key == K_w:
            self.player.vy = 0
#MOVING DOWN
        if event.type == KEYDOWN and event.key == K_s:
            self.player.vy = 300
        elif event.type == KEYUP and event.key == K_s:
            self.player.vy = 0
#MOVING RIGHT
        if event.type == KEYDOWN and event.key == K_a:
            self.player.vx = -300
        elif event.type == KEYUP and event.key == K_a:
            self.player.vx = 0
#MOVING LEFT
        if event.type == KEYDOWN and event.key == K_d:
            self.player.vx = 300
        elif event.type == KEYUP and event.key == K_d:
            self.player.vx = 0
            
#FIRING
        if event.type == KEYDOWN and event.key == K_z:
            pygame.draw.Bullet
#        elif event.type == KEYUP and event.key == K_z:
            
            

    def update(self):
        dt = min(self.min_dt, self.clock.get_time())
        self.player.update(dt)
        self.Bullet.update(dt)
    
    def draw(self, screen):
        screen.fill((0,0,0))
        screen.blit(self.player.image, self.player.rect)
        pygame.display.flip()
        Clock.tick(FPS)
        


g = Game()
g.run()

print "End of the line"

#The bad guys!
"""

class BadGuys(pygame.sprite.Sprite):
    width = 40
    height = 60

    def __init__(self,     def __init__(self, x, y, vx, vy, bounds):
        Sprite.__init__(self)

        self.vx = 0
        self.vy = 0
        self.bounds = bounds
        self.color = (255,255,0)

        self.rect = Rext(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image()

    def draw_image(self):
        self.image.fill(self.color)

    def update(self, dt):
        dt /=1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx = -self.vx
            self.rect.x += -2 * dx

        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy = -self.vy
            self.rect.y += -2 * dy


#Bad guy spawner?

class BadGuysSpawner(object):
    ship_type = Ship


    def __init__(self, duration, group, bounds):
        self.group = group
        self.bounds = bounds
        self.duration = duration
        self.time = duration
       
    def rand_vel(self):
        return 100, 100

    def rand_color(self):
        return 255,0,255

    def spawn(self):
        vx, vy = self.rand_vel()
        color = self.rand_color()

        ship = self.ship_type(x, y, vx, vy, self.bounds, color)
        self.group.add(ship)

    def update(self, dt):
        self.time += dt
        if self.time >= self.duration:
            self.time = 0
            self.spawn()
"""
