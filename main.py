import pygame, sys
from settings import *
from game_manager import Grid
from tetrominos import Tetrominos


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tetris")

    # Create the grid and tetromino
    game_grid = Grid(rows, cols, cell_size)
    tetromino = Tetrominos(cols, cell_size)

    # Timer for controlling the falling speed
    fall_timer = 0
    fall_interval = 1000 // falling_speed  # Falling interval in milliseconds

    while True:
        screen.fill((0, 153, 255))  # Background color
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    tetromino.move(1, 0)  # Move right
                elif event.key == pygame.K_LEFT:
                    tetromino.move(-1, 0)  # Move left
                elif event.key == pygame.K_UP:
                    tetromino.rotate()  # Rotate shape

        # Handle automatic falling based on timer
        if current_time - fall_timer > fall_interval:
            tetromino.move(0, 1)
            fall_timer = current_time

        # Draw the grid and tetromino
        game_grid.draw_grid(screen)
        tetromino.draw(screen)

        pygame.display.update()
        clock.tick(60)  # Fixed frame rate for smooth movement


if __name__ == '__main__':
    main()
