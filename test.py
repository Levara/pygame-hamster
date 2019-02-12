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

# Ucitavanje slika koje se koriste u igri
welcome_image = pygame.image.load("radionica-petak/shark.jpg")
start_game_image = pygame.image.load("start_game.png")
hamster_image = pygame.image.load("radionica-petak/hamster.png")
hamster_image = pygame.transform.scale(hamster_image, (100,100))

# inicijalizacija pygame sustava
pygame.init()

pygame.font.init()

#Odabir fonta i kreiranje pozdravnog teksta
myfont = pygame.font.SysFont('Arial', 40)
welcome_text = myfont.render("Welcomeee!", False, BLACK)

#Odabir fonta za tekst rezultata
score_font = pygame.font.SysFont('Arial', 20)
time_font = pygame.font.SysFont('Arial', 18)

#Score state font
score_state_font = pygame.font.SysFont('Arial', 72)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("LABUS igraa!")

clock = pygame.time.Clock()

# Varijabla koja prati rezultat
score = 0
# Varijable koje prate hamstera
hamster_x, hamster_y = 100, 100
hit = False  #Varijabla koja se postavlja kada se klikne na hamstera
original_hamster_time = 3000
hamster_time = 3000
dt = 0
#### STANJA U IGRI: start, game, score, bye
game_state = "start"
next_state = False
#Varijabla trajanja score ekrana
score_time = 5000
#Varijabla za restart igre nakon zavrsetka
restart = False
done = False
while not done:
    #event petlja
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == "bye":
                restart = True 
            if event.key == pygame.K_q:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if game_state == "start":
                if start_game_pos.collidepoint(pos):
                    next_state = True
            if game_state == "game":
                if hamster_pos.collidepoint(pos):
                    hit = True

    #Provjera i promjena stanja
    if next_state:
        next_state = False
        if game_state == "start":
            game_state = "game"
        elif game_state == "game":
            game_state = "score"
        elif game_state == "score":
            game_state = "bye"
        elif game_state == "bye":
            game_state = "game"

    #Izmjena iscrtavanja na ekranu prema odabranom stanju
    if game_state == "start":
        screen.fill( WHITE )
        screen.blit( welcome_image, (0,0))
        button_width, button_height = start_game_image.get_size()
        start_game_pos = screen.blit( start_game_image, (WIDTH/2-button_width/2,HEIGHT/2-button_height/2))
        screen.blit( welcome_text, (50, 50))
    elif game_state == "game":
        screen.fill( BLACK )
        score_text = myfont.render("Score: " + str(score), False, WHITE)
        time_text = time_font.render("Time: " + str(hamster_time), False, WHITE)
        screen.blit( score_text, (10, 10))
        screen.blit( time_text, (10, HEIGHT - 20))

        # Iscrtaj hamstera na ekran
        hamster_pos = screen.blit( hamster_image, (hamster_x, hamster_y))

        if hit:
            hit = False
            hamster_x = random.randint(100, WIDTH - 100)
            hamster_y = random.randint(100, HEIGHT - 100)
            score += 1
            hamster_time = 0.95*original_hamster_time
            original_hamster_time = hamster_time
        hamster_time -= dt
        if hamster_time <= 0:
            next_state = True

    elif game_state == "score":
        screen.fill( WHITE )
        score_state_text = score_state_font.render("Your score:" + str(score), True, BLUE)
        screen.blit( score_state_text, (WIDTH/2 - score_state_text.get_width()/2, 
                                        HEIGHT/2 - score_state_text.get_height()/2))
        score_time -= dt
        if score_time <= 0:
            next_state  = True

    elif game_state == "bye":
        screen.fill( BLUE )
        restart_text = myfont.render("Press space to restart", False, WHITE)
        screen.blit( restart_text, (10, 10))
        if restart: 
            restart = False
            hamster_time = 3000
            original_hamster_time = 3000
            score = 0
            score_time = 5000
            next_state = True


    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()
sys.exit()

