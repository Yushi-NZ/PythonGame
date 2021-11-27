import pygame
import os

# Defining window values
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

# Variables
WHITE = (255, 255 ,255)
FPS = 60

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

def main():

    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    
    # Handles main game loop
    run = True
    while run:
        # Limiting the refresh to the FPS
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Drawing the window function
        draw_window(red, yellow)

    
    # Quit game if run = False
    pygame.quit()

# Handles calling main function (safe keeping)
if __name__ == "__main__":
    main()