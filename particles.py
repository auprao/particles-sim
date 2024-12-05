import pygame

class Particle() :
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.coordinates = (x, y)
        self.radius = radius
        self.color = color

    def draw_particle(self, surface) :
        pygame.draw.circle(surface, self.color, self.coordinates, self.radius)
