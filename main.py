import pygame
import random
import sys
from Particles import *
from Colors import *
from Constants import *

# TODO : Pauli exclusion principle
# TODO : implement interaction between all particles (un-random movement)

electrons = []
protons = []
neutrons = []

def main() :

    clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption("particles sim")
    window = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
    surface = pygame.Surface((500, 500))
    window.fill(BLACK)


    for i in range(ELECTRON_COUNT) :
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)

        electron = Electron(x, y)
        electrons.append(electron)
        electron.draw_particle(surface)
        
    for i in range(PROTON_COUNT) : 
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)

        proton = Proton(x, y)
        protons.append(proton)
        proton.draw_particle(surface)

    for i in range(NEUTRON_COUNT) : 
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)

        neutron = Neutron(x, y)
        neutrons.append(neutron)
        neutron.draw_particle(surface)

    looping = True

    while looping :

        for electron in electrons :
            electron.draw_over(surface)
            electron.color = random.choice(electron.colors)
            electron.move_random(electrons)
            electron.draw_particle(surface)

        for proton in protons :
            proton.draw_over(surface)
            proton.color = random.choice(proton.colors)
            proton.move_random(protons)
            proton.draw_particle(surface)

        for neutron in neutrons :
            neutron.draw_over(surface)
            neutron.color = random.choice(neutron.colors)
            neutron.move_random(neutrons)
            neutron.draw_particle(surface)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
                looping = False

        window.blit(surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
   
       
if __name__ == "__main__":
    main()