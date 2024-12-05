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