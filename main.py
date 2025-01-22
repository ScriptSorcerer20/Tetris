import pygame, sys
from settings import *
from game_manager import Grid, draw_text, get_fall_interval
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
    state_screen(game_state)

def state_screen(game_state):
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
    """Render the pause menu"""
    screen.fill((0, 0, 0))  # Black background
    draw_text(screen, "Game Paused", 50, 450 // 2, HEIGHT // 2 - 50, (255, 255, 255))
    draw_text(screen, "Press ESC to Resume", 30, 450 // 2, HEIGHT // 2 + 10, (200, 200, 200))
    pygame.display.update()


def main():

    width = 450
    screen = pygame.display.set_mode((width, height))

    grid_surface = pygame.Surface((g_width, g_height))
    next_surface = pygame.Surface((150, 150))
    hold_surface = pygame.Surface((150, 150))

    # Create the grid and tetromino
    game_grid = Grid(rows, cols, cell_size)
    current_tetromino = Tetrominos(cols, cell_size)
    next_tetromino = Tetrominos(cols, cell_size)
    hold_tetromino = None

    hold_used = False  # Flag to track if hold has been used for the current tetromino

    fall_timer = 0

    move_timer = 0
    move_interval = 100

    while True:
        screen.fill((138, 138, 138))
        grid_surface.fill((87, 87, 87))  # Background color

        current_time = pygame.time.get_ticks()

        fall_interval = get_fall_interval(settings.game_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and settings.gamestate == "playing":
                    rotated_shape = [list(row) for row in zip(*current_tetromino.shape[::-1])]
                    if not game_grid.check_collision(rotated_shape, current_tetromino.x, current_tetromino.y):
                        current_tetromino.shape = rotated_shape  # Apply rotation
                elif event.key == pygame.K_SPACE and settings.gamestate == "playing":
                    current_tetromino.instant_drop(game_grid)  # Perform instant drop
                    game_grid.add_tetromino(current_tetromino)  # Lock tetromino in place
                    game_grid.check_full_row()
                    current_tetromino = next_tetromino
                    next_tetromino = Tetrominos(cols, cell_size)
                    hold_used = False  # Reset hold flag when a new tetromino spawns
                elif event.key == pygame.K_c and settings.gamestate == "playing":
                    if not hold_used:
                        if hold_tetromino is None:
                            hold_tetromino = current_tetromino
                            current_tetromino = next_tetromino
                            next_tetromino = Tetrominos(cols, cell_size)
                        else:
                            hold_tetromino, current_tetromino = current_tetromino, hold_tetromino
                            current_tetromino.x = cols // 2
                            current_tetromino.y = 0
                        hold_used = True

                elif event.key == pygame.K_ESCAPE:  # Pause the game
                    if settings.gamestate == "playing":
                        settings.gamestate = "paused"
                    elif settings.gamestate == "paused":
                        settings.gamestate = "playing"

        if settings.gamestate == "playing":

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if current_time - move_timer > move_interval:  # Ensure delay between movements
                    if not game_grid.check_collision(current_tetromino.shape, current_tetromino.x + 1, current_tetromino.y):
                        current_tetromino.move(1, 0)  # Move right
                    move_timer = current_time  # Reset timer
            elif keys[pygame.K_LEFT]:
                if current_time - move_timer > move_interval:  # Ensure delay between movements
                    if not game_grid.check_collision(current_tetromino.shape, current_tetromino.x - 1, current_tetromino.y):
                        current_tetromino.move(-1, 0)  # Move left
                    move_timer = current_time  # Reset timer

            # Handle automatic falling based on timer
            if current_time - fall_timer > fall_interval:
                if not game_grid.check_collision(current_tetromino.shape, current_tetromino.x, current_tetromino.y + 1):
                    current_tetromino.move(0, 1)  # Move down
                else:
                    # Collision detected, lock the tetromino in place
                    game_grid.add_tetromino(current_tetromino)
                    game_grid.check_full_row()
                    current_tetromino = next_tetromino
                    next_tetromino = Tetrominos(cols, cell_size)  # Spawn a new tetromino
                    hold_used = False

                    # Check if game is over
                    if game_grid.check_collision(current_tetromino.shape, current_tetromino.x, current_tetromino.y):
                        game_state = False
                        state_screen(game_state)

                fall_timer = current_time


            # Draw the grid and tetromino
            game_grid.draw_grid(grid_surface)
            current_tetromino.draw(grid_surface)

            # Draw the next and hold tetromino previews
            next_surface.fill((0, 0, 0))  # Clear the next surface
            next_tetromino.draw_next_tetromino(next_surface)

            hold_surface.fill((0, 0, 0))  # Clear the hold surface
            if hold_tetromino is not None:
                hold_tetromino.draw_next_tetromino(hold_surface)

            # Draw score
            draw_text(screen, f'Score: {settings.game_score}', 30, width - 75, 100, (255, 255, 255))

            # Render the surfaces
            screen.blit(grid_surface)
            screen.blit(next_surface, (width - 150, 200))
            screen.blit(hold_surface, (width - 150, 400))

            pygame.display.update()
            clock.tick(fps)

        elif settings.gamestate == "paused":
            pause_menu(screen)


if __name__ == '__main__':
    setup()