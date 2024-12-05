import random
import pygame


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
        self.shape = random.choice(self.SHAPES)  # Randomly pick a shape
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))  # Random color
        self.x = cols // 2 - len(self.shape[0]) // 2  # Center horizontally
        self.y = 0  # Start at the top

    def draw(self, screen):
        """Draw the tetromino on the screen."""
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:  # Draw only if the cell is part of the tetromino
                    x = (self.x + col_idx) * self.cell_size + 1
                    y = (self.y + row_idx) * self.cell_size + 1
                    pygame.draw.rect(
                        screen,
                        self.color,
                        pygame.Rect(x, y, self.cell_size - 2, self.cell_size - 2)
                    )

    def rotate(self):
        """Rotate the tetromino shape clockwise."""
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def move(self, dx, dy):
        """Move the tetromino."""
        self.x += dx
        self.y += dy