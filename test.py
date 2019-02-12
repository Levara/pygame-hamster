import pygame
import random
import sys

#### GLOBALNE VARIJABLE
WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

welcome_image = pygame.image.load("radionica-petak/shark.jpg")

# inicijalizacija pygame sustava
pygame.init()

pygame.font.init()

#Odabir fonta i kreiranje pozdravnog teksta
myfont = pygame.font.SysFont('Arial', 40)
welcome_text = myfont.render("Welcomeee!", False, BLACK)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("LABUS igraa!")

clock = pygame.time.Clock()

game_state = "start"
next_state = False
done = False
while not done:
    #event petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                next_state = True 
            if event.key == pygame.K_q:
                done = True
    #Provjera i promjena stanja
    if next_state:
        next_state = False
        if game_state == "start":
            game_state = "red"
        elif game_state == "red":
            game_state = "green"
        elif game_state == "green":
            game_state = "blue"
        elif game_state == "blue":
            game_state = "red"

    #Izmjena iscrtavanja na ekranu prema odabranom stanju
    if game_state == "start":
        screen.fill( WHITE )
        screen.blit( welcome_image, (0,0))
        screen.blit( welcome_text, (WIDTH/2, HEIGHT/2))
    elif game_state == "red":
        screen.fill( RED )
    elif game_state == "green":
        screen.fill( GREEN )
    elif game_state == "blue":
        screen.fill( BLUE )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

