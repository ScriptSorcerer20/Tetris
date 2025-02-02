from game.util.control import Controls_Handler
from game.util.util import load_save

width, height = 0, 0

#grid surface
g_height, g_width = 600, 300

#score
game_score = 0

actions = {"Left": False, "Right": False, "Up": False, "Down": False, "Hold": False}

save = load_save()
control_handler = Controls_Handler(save)

rows = 20
cols = 10
cell_size = 30

fps = 60

gamestate = True
