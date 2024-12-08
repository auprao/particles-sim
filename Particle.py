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
        self.is_nucleon
        self.mass

    def draw_particle(self, surface) :
        self.coordinates = (self.x, self.y)
        pygame.draw.circle(surface, self.color, self.coordinates, self.radius)

    def draw_over(self, surface) :
        pygame.draw.circle(surface, BLACK, self.coordinates, self.radius)

    def move_random(self, same_particles) :
        rand_dx = random.randrange(-1, 2)
        rand_dy = random.randrange(-1, 2)
        self.move_weighted(rand_dx, rand_dy, same_particles) 

    def move_strong_nuclear(self, same_particles, other_particles) : 
        # currently only works between neutrons and protons (good enough)
        for particle in other_particles :
            
            in_x_range = self.x > (particle.x - STRONG_INTERACTION_RANGE) and self.x < (particle.x + STRONG_INTERACTION_RANGE)
            in_y_range = self.y > (particle.y - STRONG_INTERACTION_RANGE) and self.y < (particle.y + STRONG_INTERACTION_RANGE)
            if in_x_range and in_y_range :
                self.move_towards(particle, same_particles)


    def move_electromagnetic(self, same_particles, all_particles) :
        # all_particles could be slightly optimized by taking only electric charged particles' lists
        # like the strong nuclear method
        for particle in all_particles :

            if particle.electric_charge == 0 or particle == self:
                return
            
            in_x_range = self.x > (particle.x - EM_INTERACTION_RANGE) and self.x < (particle.x + EM_INTERACTION_RANGE)
            in_y_range = self.y > (particle.y - EM_INTERACTION_RANGE) and self.y < (particle.y + EM_INTERACTION_RANGE)
            if in_x_range and in_y_range :
                if particle.electric_charge == self.electric_charge :
                    self.move_away_from(particle, same_particles)
                else : # if opposite sign
                    self.move_towards(particle, same_particles)

    def move_towards(self, particle, same_particles) :
        if (particle.x != self.x and particle.y != self.y) : # temp solution to zero division
            dx = 5 / (particle.x - self.x)
            dy = 5 / (particle.y - self.y)
            self.move_weighted(dx, dy, same_particles) 


    def move_away_from(self, particle, same_particles) :
        if (particle.x != self.x and particle.y != self.y) :
            dx = - 5 / (particle.x - self.x)
            dy = - 5 / (particle.y - self.y)
            self.move_weighted(dx, dy, same_particles) 
         

    def move_weighted(self, dx, dy, same_particles) :
        new_x = (self.x + (dx / self.mass))
        new_y = (self.y + (dy / self.mass))

        if self.can_occupy(new_x, new_y, same_particles) :
            self.x = new_x % WIDTH_WINDOW
            self.y = new_y % HEIGHT_WINDOW
        

    def can_occupy(self, x, y, same_particles) :
        for particle in same_particles :
            x_occupied = x > (particle.x - self.radius * 2) and x < (particle.x + self.radius * 2)
            y_occupied = y > (particle.y - self.radius * 2) and y < (particle.y + self.radius * 2)
            if self != particle and x_occupied and y_occupied :
                return False
        return True

    def flicker(self) :
        self.color = random.choice(self.colors)
            