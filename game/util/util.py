import pygame
import json, os

# calculate fall speed

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

# Draw text simplified

def draw_text(surface, text, font, x, y, color):
    """Utility function to render text onto a surface."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def get_background():
    return pygame.image.load('assets/menu_background.png')

#For the Leaderboard

def load_score(filename):
    """Load JSON data only if the file is not empty."""
    if os.path.exists(filename) and os.path.getsize(filename) > 0:  # Check if file exists & not empty
        with open(filename, "r") as file:
            return json.load(file)
    return {}

def add_score(filename, score):
    if os.path.exists(filename):
        with open(os.path.join(os.getcwd(), filename), "w") as file:
            json.dump(score, file)

# For keybinds (control.py)

def load_existing_save(savefile):
    with open(os.path.join(savefile), 'r+') as file:
        controls = json.load(file)
    return controls

def write_save(data):
    with open(os.path.join(os.getcwd(),'save.json'), 'w') as file:
        json.dump(data, file)

def load_save():
    try:
    # Save is loaded
        save = load_existing_save('save.json')
    except:
    # No save file, so create one
        save = create_save()
        write_save(save)
    return save


def create_save():
    new_save = {
    "controls":{
        "0" :{"Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w, "Down": pygame.K_s,
            "Start": pygame.K_RETURN, "Action1": pygame.K_SPACE},
        "1" :{"Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w, "Down": pygame.K_s,
            "Start": pygame.K_RETURN, "Action1": pygame.K_SPACE}
        },
    "current_profile": 0
    }

    return new_save

def reset_keys(actions):
    for action in actions:
        actions[action] = False
    return actions