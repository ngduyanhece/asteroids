# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame


def main():
    try:
        pygame.init()
        print('Starting asteroids!')
        pygame.quit()
    except Exception as e:
        print(f'Failed to initialize Pygame: {e}')

if __name__ == "__main__":
    main()
