import pygame
import os

# Defining window values
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

# Variables
WHITE = (255, 255 ,255)
FPS = 60
VEL = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Importing spaceship images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

# Dealing with spaceship rotation and scale 
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_window(red, yellow):

    # Drawing on window
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    pygame.display.update()

# Spaceship Movement Handlers

def yellow_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_a]: # LEFT KEY
            yellow.x -= VEL
        if keys_pressed[pygame.K_d]: # RIGHT KEY
            yellow.x += VEL
        if keys_pressed[pygame.K_w]: # UP KEY
            yellow.y -= VEL
        if keys_pressed[pygame.K_s]: # DOWN KEY
            yellow.y += VEL

def red_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_j]: # LEFT KEY
            yellow.x -= VEL
        if keys_pressed[pygame.K_l]: # RIGHT KEY
            yellow.x += VEL
        if keys_pressed[pygame.K_i]: # UP KEY
            yellow.y -= VEL
        if keys_pressed[pygame.K_k]: # DOWN KEY
            yellow.y += VEL


def main():

    # Defining spaceship transforms
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Creates clock for FPS
    clock = pygame.time.Clock()
    
    # Handles main game loop
    run = True
    while run:
        # Limiting the refresh to the FPS
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Movement for red and yellow spaceships
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        # Drawing the window function
        draw_window(red, yellow)

    
    # Quit game if run = False
    pygame.quit()

# Handles calling main function (safe keeping)
if __name__ == "__main__":
    main()