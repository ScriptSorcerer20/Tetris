import pygame as pg
from game.settings import *
from game.game_manager import Grid
from game.util import draw_text, get_fall_interval
from game.tetrominos import Tetrominos
import game.settings as settings
import sys


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.grid_surface = pg.Surface((g_width, g_height))

        self.next_surface = pg.Surface((150, 150))
        self.hold_surface = pg.Surface((150, 150))

        self.game_grid = Grid(rows, cols, cell_size)

        self.current_tetromino = Tetrominos(cols, cell_size)
        self.ghost_tetromino = Tetrominos(cols, cell_size)
        self.next_tetromino = Tetrominos(cols, cell_size)
        self.hold_tetromino = None

        self.hold_used = False  # Flag to track if hold has been used for the current tetromino

        self.fall_timer = 0
        self.move_timer = 0
        self.move_interval = 100

    def run(self):
        """Main game loop."""
        self.playing = True
        if settings.gamestate == False:
            self.game_grid = Grid(rows, cols, cell_size)
            settings.gamestate = True

        while self.playing:
            self.clock.tick(fps)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        """Handle user input and events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    rotated_shape = [list(row) for row in zip(*self.current_tetromino.shape[::-1])]
                    if not self.game_grid.check_collision(rotated_shape, self.current_tetromino.x, self.current_tetromino.y):
                        self.current_tetromino.shape = rotated_shape  # Apply rotation
                elif event.key == pg.K_SPACE:
                    self.current_tetromino.instant_drop(self.game_grid)  # Perform instant drop
                    self.lock_tetromino()
                elif event.key == pg.K_c:
                    self.handle_hold()
                elif event.key == pg.K_ESCAPE:  # Pause the game
                    self.playing = False

    def update(self):
        """Update the game state."""
        current_time = pg.time.get_ticks()
        fall_interval = get_fall_interval(settings.game_score)

        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            if current_time - self.move_timer > self.move_interval:  # Ensure delay between movements
                if not self.game_grid.check_collision(self.current_tetromino.shape, self.current_tetromino.x + 1, self.current_tetromino.y):
                    self.current_tetromino.move(1, 0)  # Move right
                self.move_timer = current_time  # Reset timer
        elif keys[pg.K_LEFT]:
            if current_time - self.move_timer > self.move_interval:  # Ensure delay between movements
                if not self.game_grid.check_collision(self.current_tetromino.shape, self.current_tetromino.x - 1, self.current_tetromino.y):
                    self.current_tetromino.move(-1, 0)  # Move left
                self.move_timer = current_time  # Reset timer

        # Handle automatic falling based on timer
        if current_time - self.fall_timer > fall_interval:
            if not self.game_grid.check_collision(self.current_tetromino.shape, self.current_tetromino.x, self.current_tetromino.y + 1):
                self.current_tetromino.move(0, 1)  # Move down
            else:
                self.lock_tetromino()

            self.fall_timer = current_time

        self.update_ghost_tetromino()

    def draw(self):
        """Render the game elements."""
        self.screen.fill((138, 138, 138))
        self.grid_surface.fill((87, 87, 87))

        # Draw the grid and tetromino
        self.game_grid.draw_grid(self.grid_surface)
        self.current_tetromino.draw(self.grid_surface)

        self.ghost_tetromino.draw_ghost_tetromino(self.grid_surface)

        # Draw next and hold previews
        self.next_surface.fill((0, 0, 0))
        self.next_tetromino.draw_next_tetromino(self.next_surface)

        self.hold_surface.fill((0, 0, 0))
        if self.hold_tetromino:
            self.hold_tetromino.draw_next_tetromino(self.hold_surface)

        # Draw score
        draw_text(self.screen, f'Score: {settings.game_score}', 30, self.width - 75, 100, (255, 255, 255))

        # Render surfaces
        self.screen.blit(self.grid_surface, (0, 0))
        self.screen.blit(self.next_surface, (self.width - 150, 200))
        self.screen.blit(self.hold_surface, (self.width - 150, 400))

        pg.display.update()

    def lock_tetromino(self):
        """Lock the current tetromino in place and spawn a new one."""
        self.game_grid.add_tetromino(self.current_tetromino)
        self.game_grid.check_full_row()
        self.current_tetromino = self.next_tetromino
        self.next_tetromino = Tetrominos(cols, cell_size)
        self.hold_used = False

        # Check for game over
        if self.game_grid.check_collision(self.current_tetromino.shape, self.current_tetromino.x, self.current_tetromino.y):
            self.show_game_over()

    def handle_hold(self):
        """Handle the hold tetromino functionality."""
        if not self.hold_used:
            if self.hold_tetromino is None:
                self.hold_tetromino = self.current_tetromino
                self.current_tetromino = self.next_tetromino
                self.next_tetromino = Tetrominos(cols, cell_size)
            else:
                self.hold_tetromino, self.current_tetromino = self.current_tetromino, self.hold_tetromino
                self.current_tetromino.x = cols // 2
                self.current_tetromino.y = 0
            self.hold_used = True

    def update_ghost_tetromino(self):
        self.ghost_tetromino.shape = self.current_tetromino.shape
        self.ghost_tetromino.x = self.current_tetromino.x
        self.ghost_tetromino.y = self.current_tetromino.y

        while not self.game_grid.check_collision(self.ghost_tetromino.shape, self.ghost_tetromino.x, self.ghost_tetromino.y + 1):
            self.ghost_tetromino.y += 1

    def show_game_over(self):
        """Handle game over screen."""
        settings.gamestate = False
        self.playing = False
