"""importing Important Modules"""

from settings import width, height
import sys
import pygame
import random


def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")

    # Set up the clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)



if __name__ == '__main__':
    main()