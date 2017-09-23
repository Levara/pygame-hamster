# ukljucivanje biblioteke pygame
import pygame
import random

#inicijalizacija pygame
pygame.init()
#inicijalizacije fontova
pygame.font.init()


# definiranje konstanti za velicinu prozora
WIDTH = 1024
HEIGHT = 600
# tuple velicine prozora
size = (WIDTH, HEIGHT)

#definiranje boja - guglaj colorpicker
WHITE= ( 255, 255, 255)
BLACK= ( 0,   0,   0  )
BLUE = (0,    0,   255)

#Renderiranje pozdravnog teksta
myfont = pygame.font.SysFont('Arial', 30)
welcome_text = myfont.render("Dobrodosli!", \
                            False, BLUE)
#daj mi velicinu welcome teksta
welcome_text_size = welcome_text.get_rect()

welcome_image = pygame.image.load( \
        "shark.jpg")

hamster = pygame.image.load("hamster.png")
hamster = pygame.transform.scale(hamster, \
                            (100, 100) )


#definiranje novog ekrana za igru
screen = pygame.display.set_mode(size)
#definiranje naziva prozora
pygame.display.set_caption("Nasa kul igra")

clock = pygame.time.Clock()

game_state = "welcome"

done = False
hit  = False
hamster_time  = 3000
hamster_x, hamster_y = 100, 100

score = 0

while not done:
    #event petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state = "game"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "game":
                pos = event.pos
                if hamster_pos.collidepoint(pos):
                    hit = True


    if game_state == "welcome":
        screen.fill(WHITE)
        screen.blit(welcome_image, (0,0) )
        screen.blit(welcome_text, ( 100, 100) )
    elif game_state == "game":
        if hit:
            hamster_time = 3000
            hamster_x = random.randint(20, WIDTH)
            hamster_y = random.randint(20, HEIGHT)
            hit = False
            score += 1

        if hamster_time < 0 :
            game_state = "game_over"

        screen.fill(WHITE)
        hamster_pos = screen.blit(hamster, \
                (hamster_x, hamster_y))
        score_text = \
                myfont.render("Score: %d!"%score, \
                False, BLUE)
        screen.blit(score_text, (10, 10) )

        hamster_time = hamster_time - clock.get_time()
    elif game_state == "game_over":
        screen.fill(BLACK)


    pygame.display.flip()
    
    #ukoliko je potrebno ceka do iscrtavanja 
    #iduceg framea kako bi imao 60fpsa
    clock.tick(60)







