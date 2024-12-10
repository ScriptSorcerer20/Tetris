import pygame, sys
from settings import *
from game_manager import Grid, draw_text
from tetrominos import Tetrominos
import settings




def setup():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((width, height))
    global clock
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tetris")
    icon_img = pygame.image.load('assets/icon.png')
    pygame.display.set_icon(icon_img)
    state_screen(screen, game_state)

def state_screen(screen, game_state):
    """Display the start screen."""
    width = 300
    screen = pygame.display.set_mode((width, height))

    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill((0, 0, 0))  # Black background

    if game_state:
        # Draw text
        draw_text(surface, "TETRIS", 50, WIDTH // 2, HEIGHT // 2 - 50, (255, 255, 255))
        draw_text(surface, "Press ENTER to Start", 30, WIDTH // 2, HEIGHT // 2 + 50, (200, 200, 200))

    else:
        draw_text(surface, "Game Over", 50, WIDTH // 2, HEIGHT // 2 - 50, (255, 0, 0))
        draw_text(surface, "Press Enter to Restart", 30, WIDTH // 2, HEIGHT // 2 + 50, (200, 200, 200))

    # Display the surface
    screen.blit(surface, (0, 0))
    pygame.display.update()

    # Wait for the player to press ENTER
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = True
                settings.game_score = 0
                main()
                return  # Exit the start screen

def pause_menu(screen):
    """Render the pause menu."""
    screen.fill((0, 0, 0))  # Black background
    draw_text(screen, "Game Paused", 50, 450 // 2, HEIGHT // 2 - 50, (255, 255, 255))
    draw_text(screen, "Press ESC to Resume", 30, 450 // 2, HEIGHT // 2 + 10, (200, 200, 200))
    pygame.display.update()


def main():

    width = 450
    screen = pygame.display.set_mode((width, height))

    grid_surface = pygame.Surface((g_width, g_height))

    # Create the grid and tetromino
    game_grid = Grid(rows, cols, cell_size)
    tetromino = Tetrominos(cols, cell_size)

    fall_timer = 0

    fall_interval = 500

    move_timer = 0
    move_interval = 100

    while True:
        screen.fill((138, 138, 138))
        grid_surface.fill((87, 87, 87))  # Background color

        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and settings.gamestate == "playing":
                    rotated_shape = [list(row) for row in zip(*tetromino.shape[::-1])]
                    if not game_grid.check_collision(rotated_shape, tetromino.x, tetromino.y):
                        tetromino.shape = rotated_shape  # Apply rotation
                elif event.key == pygame.K_SPACE and settings.gamestate == "playing":
                    tetromino.instant_drop(game_grid)  # Perform instant drop
                    game_grid.add_tetromino(tetromino)  # Lock tetromino in place
                    game_grid.check_full_row()
                    tetromino = Tetrominos(cols, cell_size)
                elif event.key == pygame.K_ESCAPE:  # Pause the game
                    if settings.gamestate == "playing":
                        settings.gamestate = "paused"
                    elif settings.gamestate == "paused":
                        settings.gamestate = "playing"

        if settings.gamestate == "playing":

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
                        game_state = False
                        state_screen(screen, game_state)

                fall_timer = current_time


            # Draw the grid and tetromino
            game_grid.draw_grid(grid_surface)
            tetromino.draw(grid_surface)

            #draw score
            draw_text(screen, f'Score: {settings.game_score}', 30, width -75, 100 , (255, 255, 255))

            screen.blit(grid_surface)

            pygame.display.update()
            clock.tick(fps)

        elif settings.gamestate == "paused":
            # Render the pause menu
            pause_menu(screen)


if __name__ == '__main__':
    setup()
