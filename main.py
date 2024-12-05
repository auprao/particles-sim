import pygame
import random
import sys
from particles import *
from colors import *
from constants import *

def main() :

    clock = pygame.time.Clock()

    pygame.init()
    window = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
    surface = pygame.Surface((500, 500))
    window.fill(BLACK)

    pygame.display.set_caption("particles sim")
    
    looping = True

    while looping :
        x = random.randrange(50, 450)
        y = random.randrange(50, 450)

        test_particle = Particle(x, y, 50, BLUE)
        test_particle.draw_particle(surface)

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