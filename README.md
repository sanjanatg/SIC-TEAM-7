# 🐍 Snake Game (Pygame)

A simple implementation of the classic Snake game built using [Pygame](https://www.pygame.org/). Control the snake, eat the food, grow longer, and avoid running into yourself or the walls!

---

## 🎮 How to Play

- Use **W / ↑** to move up  
- Use **S / ↓** to move down  
- Use **A / ←** to move left  
- Use **D / →** to move right  
- Eat the red food to grow and increase your score  
- Avoid hitting the walls or yourself!  
- If you lose, press **R** to restart the game  

---

## 🧱 Features

- Snake grows each time it eats food
- Score tracking
- Game over screen with restart prompt
- Random food placement avoiding the snake's body
- Grid background to visualize snake movement
- Snake head is white, body is dark green, and food is red

---

## 🖥️ Requirements

- Python 3.x  
- [Pygame library](https://www.pygame.org/)

## Install Pygame using pip:

```bash
pip install pygame
```

## 🚀 How to Run

Clone or download this repository
Make sure Python and Pygame are installed

Run the game with:
```bash
python snake_game.py
```

Replace snake_game.py with your actual script filename.

## 📁 File Structure

```bash
snake_game.py     # Main game logic and rendering
README.md         # Game description and instructions
```

---

## 🛠️ Code Overview

- **Snake Movement**: Controlled via arrow or WASD keys  
- **Game Grid**: 30x20 grid with each cell 20x20 pixels  
- **Game Loop**: Runs at 10 FPS, handling input, updating game state, and drawing  
- **Collision Detection**:  
  - Wall collision ends the game  
  - Self-collision ends the game  
- **Restarting**: Press `R` after a game over to restart

---

## 📄 License

This project is open-source and free to use for educational or personal use.

---

## ✏️ Author

Created by **Sanjana TG , Darshan BR & Guru Swarupa**  
Feel free to modify or improve it!
