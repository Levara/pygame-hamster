import pygame
import random

try:
    highscore_file = open("highscore", "r")
    highscore = highscore_file.readline()
    highscore = int(highscore)
except: 
    highscore = 0

print highscore

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption("Nasa igra")

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)

clock = pygame.time.Clock()
WHITE = ( 255, 255, 255)
BLACK = (   0,   0,   0)
BLUE  = (   0,   0, 255)

welcome = myfont.render("Pozdrav! pritisnite space za start!", False, BLUE)
welcome_size = welcome.get_rect()
frog = pygame.image.load("frog.jpg")

hamster = pygame.image.load("hamster.jpg")
hamster = pygame.transform.scale(hamster, (60, 60))
hamster_x = random.randint(20, WIDTH-20)
hamster_y = random.randint(20, HEIGHT-20)

game_state = "welcome"
hit  = False
done = False
hamster_time = 2000
score = 0
while not done:
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
        screen.blit(frog, (0,0) )
        screen.blit(welcome, 
                (WIDTH/2 - welcome_size.width/2,
                 HEIGHT/2 - welcome_size.height/2) )
    elif game_state == "game":
        hamster_time -= clock.get_time()

        if hit:
            hit = False
            hamster_time = 2000
            hamster_x = random.randint(20, WIDTH-20)
            hamster_y = random.randint(20, HEIGHT-20)
            score += 1
        if hamster_time <= 0:
            game_state = "game_over"

        screen.fill(BLUE)
        hamster_pos = screen.blit(hamster, 
                (hamster_x, hamster_y))
        score_text = myfont.render("Score: %d"%score, 
                                    False, WHITE)
        hscore_text = myfont.render("Highscore: %d"%highscore, False, WHITE)
        screen.blit(score_text, (0,0))
        screen.blit(hscore_text, (WIDTH/2,0))

    elif game_state == "game_over":
        screen.fill(WHITE)
        if score > highscore:
            highscore = score
        highscore_file = open("highscore", "w+")
        highscore_file.write("%d"%highscore)
        highscore_file.close()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
