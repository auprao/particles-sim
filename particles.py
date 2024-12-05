import pygame
from colors import *

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

class Electron(Particle) :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = BLUE
        self.radius = 5
