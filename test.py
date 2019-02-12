import pygame
import random
import sys

#### GLOBALNE VARIJABLE
WIDTH = 800
HEIGHT = 600


# inicijalizacija pygame sustava
pygame.init()

pygame.font.init()

pygame.display.set_mode( (WIDTH, HEIGHT) )

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(60)

pygame.quit()
sys.exit()

