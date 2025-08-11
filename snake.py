import pygame
import random
import sys

# --- Config ---
CELL_SIZE = 20
GRID_W = 30
GRID_H = 20
WIDTH = CELL_SIZE * GRID_W
HEIGHT = CELL_SIZE * GRID_H
FPS = 10  # increase to speed up the snake

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (200, 0, 0)
GRAY = (40, 40, 40)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# --- Helper functions ---
def random_food_position(snake):
    """Return a random grid cell that's not on the snake."""
    while True:
        pos = (random.randrange(GRID_W), random.randrange(GRID_H))
        if pos not in snake:
            return pos

def draw_cell(surface, pos, color):
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)

def draw_grid(surface):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRAY, (0, y), (WIDTH, y))

# --- Game ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    

    snake, direction, food, score = reset()
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    if direction != DOWN:
                        direction = UP
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    if direction != UP:
                        direction = DOWN
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    if direction != RIGHT:
                        direction = LEFT
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    if direction != LEFT:
                        direction = RIGHT
                elif event.key == pygame.K_r and game_over:
                    snake, direction, food, score = reset()
                    game_over = False

        if not game_over:
            # move snake
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            # check wall collision
            hx, hy = new_head
            if hx < 0 or hx >= GRID_W or hy < 0 or hy >= GRID_H:
                game_over = True
            else:
                # check self collision
                if new_head in snake:
                    game_over = True
                else:
                    snake.insert(0, new_head)  # add new head
                    # check food
                    if new_head == food:
                        score += 1
                        food = random_food_position(snake)
                    else:
                        snake.pop()  # remove tail

        # draw
        screen.fill(BLACK)
        draw_grid(screen)

        # draw food
        draw_cell(screen, food, RED)

        # draw snake (head brighter)
        if snake:
            draw_cell(screen, snake[0], WHITE)
            for seg in snake[1:]:
                draw_cell(screen, seg, DARK_GREEN)

        # HUD
        score_surf = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (10, 10))

        if game_over:
            go_surf = font.render("Game Over! Press R to restart or close window to quit.", True, WHITE)
            rect = go_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(go_surf, rect)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
