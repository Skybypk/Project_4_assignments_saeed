import pygame
import time

# Initialize pygame
pygame.init()

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 182, 193)

# Set up the display
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Eraser Effect in pygame")

# Create grid
grid = []
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):  # Fixed: Changed CANVAS_HEIGHT to CANVAS_WIDTH
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

# Initialize eraser
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)  # Fixed: Added proper size and position

running = True
while running:
    screen.fill(WHITE)
    
    # Draw grid
    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)
        pygame.draw.rect(screen, WHITE, rect, 1)  # Add grid lines
    
    # Get mouse position and update eraser
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x - ERASER_SIZE//2, mouse_y - ERASER_SIZE//2)  # Center eraser on mouse
    
    # Check collisions and create new grid
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):  # Fixed: Changed collid to colliderect
            new_grid.append(rect)
        else:
            pygame.draw.rect(screen, WHITE, rect)  # Erase by drawing white
    
    grid = new_grid
    
    # Draw eraser
    pygame.draw.rect(screen, PINK, eraser)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
