import pygame
import random # hopefully deletable later.
from constants import *
from colors import *

# can come back to using self.coordinates = (x, y) if not a problem
class Particle() :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color
        self.radius

    def draw_particle(self, surface) :
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    def draw_over(self, surface) :
        pygame.draw.circle(surface, BLACK, (self.x, self.y), self.radius)
    def move_random(self) :
        self.x = (self.x + random.randrange(-2, 3)) % WIDTH_WINDOW 
        self.y = (self.y + random.randrange(-2, 3)) % HEIGHT_WINDOW

class Electron(Particle) :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BLUE
        self.radius = 3

class Proton(Particle) :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED
        self.radius = 6