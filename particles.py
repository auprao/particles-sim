import pygame
from colors import *

class Particle() :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)
        self.color
        self.radius

    def draw_particle(self, surface) :
        pygame.draw.circle(surface, self.color, self.coordinates, self.radius)

class Electron(Particle) :
    def __init__(self, x, y):
        self.color = BLUE
        self.radius = 5
        super().__init__(x, y)
