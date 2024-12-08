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
        self.electric_charge
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

    def move_electromagnetic(self, all_particles, same_particles) :
        # all_particles could be optimized by taking only electric charged particles' lists
        for particle in all_particles :

            if particle.electric_charge == 0 or particle == self:
                return
            
            in_x_range = self.x > (particle.x - INTERACTION_RANGE) and self.x < (particle.x + INTERACTION_RANGE)
            in_y_range = self.y > (particle.y - INTERACTION_RANGE) and self.y < (particle.y + INTERACTION_RANGE)
            if in_x_range and in_y_range :
                if particle.electric_charge == self.electric_charge :
                    self.move_away_from(particle, same_particles)
                else : # if opposite sign - probably doesn't need extra elif check
                    self.move_towards(particle, same_particles)

    def move_towards(self, particle, particles) :
        return

    def move_away_from(self, particle, particles) :
        return             

    def move_weighted(self, dx, dy, particles) :
        new_x = (self.x + (dx / self.mass))
        new_y = (self.y + (dy / self.mass))

        if self.can_occupy(new_x, new_y, particles) :
            self.x = new_x % WIDTH_WINDOW
            self.y = new_y % HEIGHT_WINDOW
        

    def can_occupy(self, x, y, particles) :
        for particle in particles :
            x_occupied = x > (particle.x - self.radius * 2) and x < (particle.x + self.radius * 2)
            y_occupied = y > (particle.y - self.radius * 2) and y < (particle.y + self.radius * 2)
            if self != particle and x_occupied and y_occupied :
                return False
        return True
            