import pygame
import numpy as np
import sys
import random

# Config
CELL_SIZE = 4
GRID_WIDTH = 250
GRID_HEIGHT = 200
FPS = 100  # You can now go much higher

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Conway's Game of Life (Optimized)")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)

# Create random grid
def create_grid():
    return np.random.choice([0, 1], size=(GRID_HEIGHT, GRID_WIDTH), p=[0.8, 0.2]).astype(np.uint8)

# Get next generation using NumPy magic
def next_generation(grid):
    neighbors = sum(np.roll(np.roll(grid, dx, axis=0), dy, axis=1)
                    for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                    if (dx != 0 or dy != 0))

    birth = (neighbors == 3) & (grid == 0)
    survive = ((neighbors == 2) | (neighbors == 3)) & (grid == 1)
    return (birth | survive).astype(np.uint8)

# Draw grid + FPS
def draw_grid(grid, fps):
    screen.fill(BLACK)
    live_cells = np.argwhere(grid == 1)
    for x, y in live_cells:
        rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, rect)

    # FPS text
    fps_text = font.render(f"FPS: {int(fps)}", True, GREEN)
    screen.blit(fps_text, (5, 5))
    pygame.display.flip()

# Main loop
def main():
    grid = create_grid()
    running = True

    while running:
        dt = clock.tick(FPS)
        fps_now = clock.get_fps()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid = create_grid()

        draw_grid(grid, fps_now)
        grid = next_generation(grid)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
