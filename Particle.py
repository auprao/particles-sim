import pygame
import random
from Constants import *
from Colors import *
import Particles

class Particle() :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)
        self.color
        self.colors
        self.radius
        self.mass

    def draw_particle(self, surface) :
        self.coordinates = (self.x, self.y)
        pygame.draw.circle(surface, self.color, self.coordinates, self.radius)

    def draw_over(self, surface) :
        pygame.draw.circle(surface, BLACK, self.coordinates, self.radius)

    def move_random(self, particles) :
        rand_x = random.randrange(-2, 3)
        rand_y = random.randrange(-2, 3)
        self.move_weighted(rand_x, rand_y, particles) 

    def move_weighted(self, dx, dy, particles) :
        new_x = (self.x + (dx / self.mass))
        new_y = (self.y + (dy / self.mass))

        if self.can_occupy(new_x, new_y, particles) :
            self.x = new_x % WIDTH_WINDOW
            self.y = new_y % HEIGHT_WINDOW


    def can_occupy(self, x, y, particles) :
        # can be optimized to not iterate through other particle
        for particle in particles :
            x_occupied = x > (particle.x - self.radius * 2) and x < (particle.x + self.radius * 2)
            y_occupied = y > (particle.y - self.radius * 2) and y < (particle.y + self.radius * 2)
            if self != particle and x_occupied and y_occupied :
                return False
        return True
            