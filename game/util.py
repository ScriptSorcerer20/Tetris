import pygame

def get_fall_interval(score):
    """
    Calculate the fall interval based on the current score.
    """
    base_interval = 1000  # Base interval in milliseconds
    decrease_per_1000_points = 50  # Decrease in ms per 1000 points
    min_interval = 100  # Minimum interval in milliseconds

    # Calculate the fall interval
    interval = base_interval - (score // 400) * decrease_per_1000_points

    # Ensure the interval doesn't go below the minimum
    return max(interval, min_interval)

#game states
def draw_text(surface, text, size, x, y, color):
    """Utility function to render text onto a surface."""
    font = pygame.font.Font(None, size)  # Use default font
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)