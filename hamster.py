# ukljucivanje biblioteke pygame
import pygame

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

#definiranje novog ekrana za igru
screen = pygame.display.set_mode(size)
#definiranje naziva prozora
pygame.display.set_caption("Nasa kul igra")

clock = pygame.time.Clock()

game_state = "welcome"

done = False
while not done:
    #event petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state = "game"

    if game_state == "welcome":
        screen.fill(WHITE)
        screen.blit(welcome_image, (0,0) )
        screen.blit(welcome_text, ( 100, 100) )
    elif game_state == "game":
        screen.fill(BLUE)


    pygame.display.flip()
    
    #ukoliko je potrebno ceka do iscrtavanja 
    #iduceg framea kako bi imao 60fpsa
    clock.tick(60)







