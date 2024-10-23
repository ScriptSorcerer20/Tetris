# Tetris

## Introduction: A Journey in Code

What started as a quest to sharpen my Python skills quickly became something much more exciting. I had brainstormed countless project ideas, but none of them truly matched my abilities or ignited my passion—until inspiration struck. Tetris.

The idea hit me like a falling tetromino, and I realized immediately it was the perfect fit. Simple at its core, yet challenging enough to push my skills, it embodied everything I was looking for. Not only is it a timeless and addictively fun game, but it's also the ideal starting point for diving into Pygame, a project that wouldn't rely on step-by-step tutorials.

This isn't just about coding; it's about building something I love from the ground up. And honestly? Writing this intro was almost as fun as watching the pieces fall into place!
**May my Journey begin**


## Structure

Tetris/  
│  
├── main.py            # Hauptskript für das Spiel  
├── tetrominos.py        # Tetromino-Klassen und Logik  
├── game_manager.py      # Spiellogik (Grid, Zeilen löschen, Spielstatus)  
├── settings.py          # Einstellungen (Farben, Größe, Geschwindigkeit)  
├── assets/              # Ordner für Assets wie Bilder, Sounds (falls verwendet)  
│   └── sounds/  
└── README.md            # Projektbeschreibung (optional)  


## Functionalities

### **1. Tetromino Generation**
   - **Random Tetromino Shapes**: Start by coding the logic to generate the 7 classic Tetromino shapes (I, O, T, L, J, S, Z). Each shape can be represented as a matrix.
   - **Random Color Assignment**: Assign a unique color to each Tetromino for visual differentiation. This can be handled right after generating the shapes.

### **2. Grid Setup (Playfield)**
   - **Create the Grid**: Implement the game grid as a 2D array where the blocks will fall. This grid should match the Tetris field size (usually 10x20).
   - **Grid Drawing**: Write the code to render the grid and the Tetrominoes inside the grid. This will help visualize your game's progress.

### **3. Tetromino Movement**
   - **Horizontal Movement**: Implement the left and right movement of the falling Tetromino using the arrow keys. This will allow basic player control.
   - **Vertical Movement**: Implement automatic downward movement for the falling Tetromino at regular intervals. This is the fundamental mechanic that drives the game forward.
   - **Soft Drop**: Implement the ability to accelerate the fall of the Tetromino using the down arrow key.
   - **Hard Drop**: Implement the hard drop feature where pressing a key (e.g., spacebar) instantly drops the Tetromino to the bottom of the grid.

### **4. Tetromino Rotation**
   - **Clockwise Rotation**: Implement logic to rotate the Tetromino 90 degrees clockwise when the player presses a key (e.g., up arrow). Ensure the rotation works for all shapes.
   - **Rotation Collision Check**: Make sure the Tetromino doesn’t rotate into walls or other blocks. You might need a "wall kick" system to adjust their position slightly after rotation.

### **5. Collision Detection**
   - **Bottom Collision**: Implement the logic to stop a Tetromino when it collides with the bottom of the grid. This prevents the Tetromino from falling out of bounds.
   - **Side Collision**: Ensure the Tetromino stops moving sideways if it hits the left or right walls of the grid.
   - **Stack Collision**: Implement the logic to stop the Tetromino from falling when it lands on top of other blocks already placed in the grid.

### **6. Tetromino Locking (Placing)**
   - **Lock Tetromino in Place**: Once a Tetromino reaches the bottom or hits another block, place it permanently on the grid. This will be the key moment when the game moves from one Tetromino to the next.
   - **Generate New Tetromino**: After a Tetromino is locked in place, immediately generate a new random Tetromino and drop it from the top of the grid.

### **7. Line Clearing**
   - **Full Line Detection**: Implement the logic to detect when a row in the grid is fully filled with blocks.
   - **Remove Full Lines**: Once a row is detected as full, remove it and shift all rows above it downward.
   - **Score Increment**: Increment the player’s score every time a line is cleared. You can start simple by giving a fixed score for each line cleared.

### **8. Level Progression**
   - **Leveling Up**: Implement the logic to increase the game’s level after a certain number of lines are cleared. You can, for example, increase the level after every 10 lines.
   - **Speed Increase**: As the level increases, decrease the time interval between automatic downward movements of the Tetromino, making the game harder.

### **9. Game Over**
   - **Game Over Condition**: Implement the game-over condition when a new Tetromino cannot be placed because the blocks have reached the top of the grid.
   - **Game Over Screen**: Display a simple game-over screen with an option to restart or quit the game.


## Additional Functionalities

#### a) **Score System**
   - **Combo Scoring**: Award bonus points for clearing multiple lines simultaneously (e.g., double, triple, or Tetris for clearing 4 lines).
   - **Soft Drop Scoring**: Give points for soft dropping (incremental points as the Tetromino moves down).
   - **Hard Drop Scoring**: Award more points for hard dropping a Tetromino instantly.

#### b) **Next Tetromino Preview**
   - **Show Upcoming Tetromino**: Display the next Tetromino in a small box on the screen so the player can prepare for it.

#### c) **Hold Functionality**
   - **Hold a Tetromino**: Allow the player to "hold" a Tetromino and swap it with the current falling Tetromino.
   - **One Swap per Tetromino**: Restrict the hold functionality to one swap per Tetromino fall.

#### d) **Pause/Resume Functionality**
   - **Pause the Game**: Allow the player to pause and resume the game (usually with the Escape key).

#### e) **Sound Effects and Music**
   - **Block Movement Sounds**: Play sounds when the Tetromino moves or rotates.
   - **Line Clearing Sound**: Add a special sound effect when a line is cleared.
   - **Background Music**: Play looped background music during the game.

#### f) **Themes and Skins**
   - **Different Tetromino Skins**: Allow the player to change the appearance of the Tetrominos (colors, textures).
   - **Background Themes**: Change the game background based on the level or user selection.

#### g) **High Score Tracking**
   - **Save High Scores**: Keep track of the player's highest scores, even after closing the game.
   - **Leaderboard**: Display a leaderboard showing the top scores.

#### h) **Difficulty Settings**
   - **Adjustable Difficulty**: Allow the player to select a difficulty level at the start (easy, medium, hard), which affects fall speed and scoring.
   - **Challenge Modes**: Add special game modes with unique rules, such as "Endless Mode," "Timed Mode," or "Puzzle Mode" (pre-defined Tetrominoes to clear lines with).

#### i) **Ghost Piece**
   - **Ghost Piece Display**: Show a transparent outline of where the Tetromino will land if it were to fall straight down.

#### j) **Achievements**
   - **Unlockable Achievements**: Reward players for achieving specific goals, such as clearing a certain number of lines, reaching a high score, or playing multiple games.

#### k) **Multiplayer Mode**
   - **Local Multiplayer**: Add a two-player mode where players compete on the same screen, each having their own grid.
   - **Competitive Multiplayer**: Send garbage lines to the opponent when you clear multiple lines (similar to modern Tetris games).
   - **Online Multiplayer**: Implement online matchmaking or P2P multiplayer mode (advanced feature).

#### l) **Animation and Visual Effects**
   - **Line Clear Animation**: Add an animation when lines are cleared (e.g., blocks fade out or explode).
   - **Special Effects for Tetris**: Show a special visual effect when the player clears four lines at once.

#### m) **Customizable Controls**
   - **Control Remapping**: Allow the player to customize key bindings for moving, rotating, and dropping Tetrominos.

#### n) **Statistics**
   - **Track Player Stats**: Display detailed player stats such as total lines cleared, Tetrominoes dropped, and total playtime.
