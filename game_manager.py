import pygame

class Grid():
    def __init__(self, rows, cols, cell_size):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for j in range(self.cols)] for k in range(self.rows)]

    def draw_grid(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_value = self.grid[row][col]
                color = (0, 0, 0) if cell_value == 0 else (255, 0, 0)  # Black for empty, red for filled
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
                        self.grid[grid_y][grid_x] = 1

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
        """Check for and clear any full rows."""
        new_grid = [row for row in self.grid if not all(cell == 1 for cell in row)]
        cleared_rows = len(self.grid) - len(new_grid)
        self.grid = [[0] * self.cols for _ in range(cleared_rows)] + new_grid
