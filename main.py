import pygame
import random
import sys
from particles import *
from colors import *
from constants import *

# TODO : Pauli exclusion principle
# TODO : interaction table
# TODO : implement interaction bevery all particles (un-random movement)

def main() :

    clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption("particles sim")
    window = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
    surface = pygame.Surface((500, 500))
    window.fill(BLACK)


    electrons = []
    for i in range(PARTICLE_COUNT) :
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)

        electron = Electron(x, y)
        electrons.append(electron)
        electron.draw_particle(surface)
        
    protons = []
    for i in range(10) : 
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)

        proton = Proton(x, y)
        protons.append(proton)
        proton.draw_particle(surface)

    looping = True

    while looping :

        for electron in electrons :
            electron.draw_over(surface)
            electron.color = random.choice((BLUE, WHITE))
            electron.move_random()
            electron.draw_particle(surface)

        for proton in protons :
            proton.draw_over(surface)
            proton.color = random.choice((RED, ORANGE))
            proton.move_random()
            proton.draw_particle(surface)

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