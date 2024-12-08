import pygame
import random
import sys
from Particles import *
from Colors import *
from Constants import *

# TODO : particles shouldn't overlap on spawn (add checker to spawn methods)

electrons = []
protons = []
neutrons = []
all_particles = []

def main() :

    clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption("particles sim")
    window = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
    surface = pygame.Surface((500, 500))
    window.fill(BLACK)

    spawn(electrons, Electron, ELECTRON_COUNT, surface)
    spawn(protons, Proton, PROTON_COUNT, surface)
    spawn(neutrons, Neutron, NEUTRON_COUNT, surface)

    all_particles.extend(electrons)
    all_particles.extend(protons)
    all_particles.extend(neutrons)

    looping = True

    while looping :

        move(electrons, all_particles, surface)
        move(protons, all_particles, surface)
        move(neutrons, all_particles, surface)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
                looping = False

        window.blit(surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
   
def spawn(same_particles, type, count, surface) :
    for i in range(count) :
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)

        particle = type(x, y)
        same_particles.append(particle)
        particle.draw_particle(surface)
       
def move(same_particles, all_particles, surface) :

    for particle in same_particles :
        particle.flicker()
        particle.move_random(same_particles)
    
    if same_particles[0].electric_charge != 0 : # electrons and protons
        for particle in same_particles :
            particle.move_electromagnetic(all_particles, same_particles)

        if same_particles[0].is_nucleon : # protons
            for particle in same_particles :
                particle.move_strong_nuclear(neutrons, same_particles)

    elif same_particles[0].is_nucleon : # neutrons
        for particle in same_particles :
            particle.move_strong_nuclear(protons, same_particles)

    for particle in same_particles :
        particle.draw_over(surface)
        particle.draw_particle(surface)


if __name__ == "__main__":
    main()