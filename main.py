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

    fall_timer = 0
    fall_interval = 1000 // falling_speed  # Falling interval in milliseconds

    move_timer = 0
    move_interval = 100

    while True:
        screen.fill((0, 153, 255))  # Background color
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rotated_shape = [list(row) for row in zip(*tetromino.shape[::-1])]
                    if not game_grid.check_collision(rotated_shape, tetromino.x, tetromino.y):
                        tetromino.shape = rotated_shape  # Apply rotation

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if current_time - move_timer > move_interval:  # Ensure delay between movements
                if not game_grid.check_collision(tetromino.shape, tetromino.x + 1, tetromino.y):
                    tetromino.move(1, 0)  # Move right
                move_timer = current_time  # Reset timer
        elif keys[pygame.K_LEFT]:
            if current_time - move_timer > move_interval:  # Ensure delay between movements
                if not game_grid.check_collision(tetromino.shape, tetromino.x - 1, tetromino.y):
                    tetromino.move(-1, 0)  # Move left
                move_timer = current_time  # Reset timer

        # Handle automatic falling based on timer
        if current_time - fall_timer > fall_interval:
            if not game_grid.check_collision(tetromino.shape, tetromino.x, tetromino.y + 1):
                tetromino.move(0, 1)  # Move down
            else:
                # Collision detected, lock the tetromino in place
                game_grid.add_tetromino(tetromino)
                game_grid.check_full_row()
                tetromino = Tetrominos(cols, cell_size)  # Spawn a new tetromino

                # Check if game is over
                if game_grid.check_collision(tetromino.shape, tetromino.x, tetromino.y):
                    print("Game Over")
                    sys.exit()

            fall_timer = current_time

        # Draw the grid and tetromino
        game_grid.draw_grid(screen)
        tetromino.draw(screen)

        pygame.display.update()
        clock.tick(60)  # Fixed frame rate for smooth movement


if __name__ == '__main__':
    main()
