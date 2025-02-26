import pygame
from game.tetrominos import set_color
import game.settings as settings

class Grid():
    def __init__(self, rows, cols, cell_size):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.color = set_color()
        self.grid = [[0 for j in range(self.cols)] for k in range(self.rows)]

        self.cleared_rows = []

    def draw_grid(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                if cell_value == 0:
                    color = (0, 0, 0)
                elif cell_value == 1:
                    color = self.color[0]
                elif cell_value == 2:
                    color = self.color[1]
                elif cell_value == 3:
                    color = self.color[2]
                elif cell_value == 4:
                    color = self.color[3]
                elif cell_value == 5:
                    color = self.color[4]
                elif cell_value == 6:
                    color = self.color[5]
                else:
                    color = self.color[6]

                cell_rect = pygame.Rect(
                    col * self.cell_size + 1,
                    row * self.cell_size + 1,
                    self.cell_size - 2,
                    self.cell_size - 2
                )
                pygame.draw.rect(surface, color, cell_rect)

    def add_tetromino(self, tetromino):
        """Lock the tetromino into the grid."""
        for row_idx, row in enumerate(tetromino.shape):
            for col_idx, cell in enumerate(row):
                if cell:  # Only lock non-empty cells
                    grid_x = tetromino.x + col_idx
                    grid_y = tetromino.y + row_idx
                    if 0 <= grid_y < self.rows and 0 <= grid_x < self.cols:
                        self.grid[grid_y][grid_x] = tetromino.shape_number

    def check_collision(self, shape, x, y):
        """Check if the tetromino collides with the grid or boundaries."""
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:  # Only check cells that are part of the tetromino
                    grid_x = x + col_idx
                    grid_y = y + row_idx

                    # Check bounds
                    if grid_x < 0 or grid_x >= self.cols or grid_y >= self.rows:
                        return True

                    # Check if cell is already occupied
                    if grid_y >= 0 and self.grid[grid_y][grid_x] != 0:
                        return True

    def check_full_row(self):
        """Check for and store full rows for animation before clearing them."""
        self.cleared_rows = [i for i, row in enumerate(self.grid) if all(cell != 0 for cell in row)]

        if self.cleared_rows:
            self.clearing_animation_timer = pygame.time.get_ticks()  # Start animation timer

    def animate_line_clear(self, screen):
        """Handles the visual effect when clearing rows."""
        if not self.cleared_rows:
            return

        elapsed_time = pygame.time.get_ticks() - self.clearing_animation_timer

        if elapsed_time < 500:  # Animation lasts 500ms
            fade_alpha = int(255 * (1 - elapsed_time / 500))  # Fading effect
            if elapsed_time > 400:
                fade_color = (0, 0, 0, fade_alpha)  # White fading color
            elif elapsed_time > 300:
                fade_color = (100, 100, 100, fade_alpha)
            elif elapsed_time > 200:
                fade_color = (150, 150, 150, fade_alpha)
            elif elapsed_time > 100:
                fade_color = (200, 200, 200, fade_alpha)
            else:
                fade_color = (255, 255, 255, fade_alpha)

            for row in self.cleared_rows:
                for col in range(self.cols):
                    rect = pygame.Rect(col * self.cell_size + settings.width // 2 -150, row * self.cell_size +50, self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, fade_color[:3], rect)
                    pygame.draw.rect(screen, (0, 0, 0), rect, 1)
        else:
            self.clear_rows()  # Remove rows after animation is complete

    def clear_rows(self):
        """Removes full rows after the animation finishes."""
        new_grid = [row for i, row in enumerate(self.grid) if i not in self.cleared_rows]
        cleared_count = len(self.cleared_rows)

        # Add empty rows at the top
        self.grid = [[0] * self.cols for _ in range(cleared_count)] + new_grid

        score_table = {1: 100, 2: 300, 3: 500, 4: 800}
        settings.game_score += score_table.get(len(self.cleared_rows), 0)
        self.cleared_rows = []  # Reset after clearing
