import pygame
import random
import sys

pygame.init()

pygame.font.init()

pygame.display.set_mode( (1024, 600) )

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(60)

pygame.quit()
sys.exit()

