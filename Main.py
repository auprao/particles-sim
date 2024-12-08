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
   
def spawn(type_list, type, count, surface) :
    for i in range(count) :
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)

        particle = type(x, y)
        type_list.append(particle)
        particle.draw_particle(surface)
       
def move(type_list, all_particles, surface) :
    
    #particle.move_strong_nuclear(all_particles, type_list)

    for particle in type_list :
        particle.flicker()
        particle.move_random(type_list)
    
    if type_list[0].electric_charge != 0 :
        for particle in type_list :
            particle.move_electromagnetic(all_particles, type_list)

    for particle in type_list :
        particle.draw_over(surface)
        particle.draw_particle(surface)


if __name__ == "__main__":
    main()