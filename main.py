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
    while True:
        # Event handling to check if the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop if the user closes the window

        # Fill the screen with black color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
