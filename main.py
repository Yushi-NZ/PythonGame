import pygame
import os

from pygame.constants import WINDOWENTER
pygame.font.init()
pygame.mixer.init()

# Defining window values
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

# Colours
WHITE = (255, 255 ,255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)

# Variables
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

# Importing fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)


BORDER = pygame.Rect(WIDTH//2 - 5 , 0, 10, HEIGHT)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# SFX
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

# Events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Importing spaceship images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

# Importing and scaling background image
SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join(
        'Assets', 'space.png')), (WIDTH, HEIGHT))

# Dealing with spaceship rotation and scale 
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):

    # Creating the background and border
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    # Creating the text object
    red_health_text = HEALTH_FONT.render('Red Health: ' + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render('Yellow Health: ' + str(yellow_health), 1, WHITE)

    # Drawing "Health: " text for both Yellow and Red spaceships
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    # Drawing the Red and Yellow spaceships
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    # Drawing Red bullets
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    # Drawing Yellow Bullets
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    # Updating the display (drawing)
    pygame.display.update()

# Spaceship Movement Handlers
def yellow_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # YELLOW LEFT KEY
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # YELLOW RIGHT KEY
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # YELLOW UP KEY
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT -15: # YELLOW DOWN KEY
            yellow.y += VEL

def red_movement(keys_pressed, red):
        if keys_pressed[pygame.K_j] and red.x - VEL > BORDER.x + BORDER.width: # RED LEFT KEY
            red.x -= VEL
        if keys_pressed[pygame.K_l] and red.x + VEL + red.width < WIDTH: # RED RIGHT KEY
            red.x += VEL
        if keys_pressed[pygame.K_i] and red.y - VEL > 0: # RED UP KEY
            red.y -= VEL
        if keys_pressed[pygame.K_k] and red.y + VEL + red.height < HEIGHT -15: # RED DOWN KEY
            red.y += VEL

# Deals with bullet collisions
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):

    # Creating the winner text
    winner_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(winner_text, (WIDTH/2 - winner_text.get_width()/2, HEIGHT/2 - winner_text.get_height()/2))
    
    # Updating and pausing for 5000ms
    pygame.display.update()
    pygame.time.delay(5000)

def main():

    # Defining spaceship transforms
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Bullets arrays
    red_bullets = []
    yellow_bullets = []

    red_health = 6
    yellow_health = 6

    # Creates clock for FPS
    clock = pygame.time.Clock()
    
    # Handles main game loop
    run = True
    while run:
        # Limiting the refresh to the FPS
        clock.tick(FPS)
        for event in pygame.event.get():
            # Handles quitting game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            # Handling shooting
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            # Handling hit events
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        # Yellow Wins    
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        # Red Wins
        if yellow_health <= 0:
            winner_text = "Red Wins!"

        # Draw winnter
        if winner_text != "":
            draw_winner(winner_text)
            break

        # Movement for red and yellow spaceships
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        # Handles Bullets
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # Drawing the window function
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    # Restarting game
    main()

# Handles calling main function (safe keeping)
if __name__ == "__main__":
    main()