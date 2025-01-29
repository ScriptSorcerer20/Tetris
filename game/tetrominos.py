import random
import pygame

def set_color():
    yellow = (255, 255, 0)
    violet = (204, 0, 204)
    green = (0, 153, 0)
    orange = (255, 153, 0)
    light_blue = (0, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    colors = [yellow, violet, green, orange, light_blue, red, blue]
    return colors


class Tetrominos:
    SHAPES = [
        [[1, 1, 1, 1]],                  # I-shape
        [[1, 1], [1, 1]],                # O-shape
        [[0, 1, 0], [1, 1, 1]],          # T-shape
        [[1, 0, 0], [1, 1, 1]],          # L-shape
        [[0, 0, 1], [1, 1, 1]],          # J-shape
        [[0, 1, 1], [1, 1, 0]],          # S-shape
        [[1, 1, 0], [0, 1, 1]],          # Z-shape
    ]

    def __init__(self, cols, cell_size):
        self.cell_size = cell_size
        self.shape_number = random.choice([1, 2, 3, 4, 5, 6, 7])  # Randomly pick a shape
        self.shape = self.SHAPES[self.shape_number - 1]
        self.colors = set_color()
        self.x = cols // 2 - len(self.shape[0]) // 2  # Center horizontally
        self.y = 0



    def draw(self, screen):
        """Draw the tetromino on the screen."""
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:  # Draw only if the cell is part of the tetromino
                    x = (self.x + col_idx) * self.cell_size + 1
                    y = (self.y + row_idx) * self.cell_size + 1
                    pygame.draw.rect(
                        screen,
                        self.colors[self.shape_number - 1],
                        pygame.Rect(x, y, self.cell_size - 2, self.cell_size - 2)
                    )

    def rotate(self):
        """Rotate the tetromino shape clockwise."""
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def move(self, dx, dy):
        """Move the tetromino."""
        self.x += dx
        self.y += dy

    def instant_drop(self, grid):
        """Move the tetromino to the lowest possible position."""
        while not grid.check_collision(self.shape, self.x, self.y + 1):
            self.y += 1

    def draw_next_tetromino(self, surface):
        """
        Draw the next tetromino in the preview window.
        """
        surface.fill((0, 0, 0))

        cell_size = 30  # Smaller cell size for the preview
        x_offset = (surface.get_width() - len(self.shape[0]) * cell_size) // 2
        y_offset = (surface.get_height() - len(self.shape) * cell_size) // 2

        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    cell_rect = pygame.Rect(
                        x_offset + col_idx * cell_size,
                        y_offset + row_idx * cell_size,
                        cell_size,
                        cell_size
                    )
                    pygame.draw.rect(surface, self.colors[self.shape_number - 1], cell_rect)

    def draw_ghost_tetromino(self, screen):
        """Draw the tetromino on the screen."""
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = (self.x + col_idx) * self.cell_size + 1
                    y = (self.y + row_idx) * self.cell_size + 1
                    rect = pygame.Rect(x, y, self.cell_size - 2, self.cell_size - 2)
                    pygame.draw.rect(screen, (61, 61, 61), rect)
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)

