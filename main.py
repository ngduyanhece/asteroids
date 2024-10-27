# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()  # Initialize Pygame

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Start the game loop
    clock = pygame.time.Clock()
    while True:
        clock.tick(60) 
        # Event handling to check if the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:

        # Fill the screen with black color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()
        pygame.time.delay(10)  # Add a small delay to reduce CPU usage

if __name__ == "__main__":
    main()
