# Snake Game (Python)

This is a classic Snake game developed using Python. The game is designed with a modular structure, where different parts of the game are separated into individual Python files for better organization and readability. The player controls a snake that moves around the screen, eats food to grow longer, and scores points while avoiding collisions with the walls or its own body. High scores are stored in a `data.txt` file to keep track of the player’s best performance.

The project includes separate modules for the main game loop, snake behavior, food generation, and the scoreboard system.

## Features
- Classic Snake gameplay
- Modular code structure
- Snake growth when food is eaten
- Score tracking with high score saved in `data.txt`
- Smooth snake movement
- Simple and responsive keyboard controls

## Technologies Used
- Python 3
- Turtle (Python built-in library)

## Project Structure
```
main.py         # Main game loop and screen setup
snake.py        # Snake movement and growth logic
food.py         # Food creation and positioning
scoreboard.py   # Score display and tracking
data.txt        # Stores the high score
README.md
```

## How to Run
1. Make sure Python 3 is installed on your system.  
2. Keep all `.py` files and `data.txt` in the same folder.  
3. Run the game using:

```
python main.py
```

## Controls
- Up Arrow: Move Up  
- Down Arrow: Move Down  
- Left Arrow: Move Left  
- Right Arrow: Move Right  

## Author
Alex
