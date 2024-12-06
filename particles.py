import pygame
import random
from constants import *
from colors import *

# can come back to using self.coordinates = (x, y) if not a problem
class Particle() :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color
        self.colors
        self.radius
        self.mass

    def draw_particle(self, surface) :
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    def draw_over(self, surface) :
        pygame.draw.circle(surface, BLACK, (self.x, self.y), self.radius)
    def move_random(self) :
        rand_x = random.randrange(-2, 3)
        rand_y = random.randrange(-2, 3)
        self.move_weighted(rand_x, rand_y) 
    def move_weighted(self, dx, dy) :
        self.x = (self.x + (dx / self.mass) ) % WIDTH_WINDOW
        self.y = (self.y + (dy / self.mass) ) % HEIGHT_WINDOW


class Electron(Particle) :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BLUE
        self.colors = [BLUE, WHITE]
        self.radius = 3
        self.electric_charge = -1
        self.mass = 1

class Proton(Particle) :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED
        self.colors = [RED, ORANGE]
        self.radius = 6
        self.electric_charge = +1
        self.mass = 10

class Neutron(Particle) :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = DARK_GRAY
        self.colors = [DARK_GRAY, LIGHT_GRAY]
        self.radius = 5
        self.electric_charge = 0
        self.mass = 8