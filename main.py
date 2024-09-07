import pygame
from motorx import Motorx
from motory import Motory

# Setup display
pygame.init()
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver!")

# Load the sudoku image
sudoku_img = pygame.image.load('imgs/sudoku.jpg')

# Optional: Scale the image to fit the window (if needed)
sudoku_img = pygame.transform.scale(sudoku_img, (300, 300))

# Setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

motorx = Motorx()
motory = Motory(motorx.x)

# Movement speed
move_speed = 5

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
        
    # Get keys pressed for continuous movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        motorx.move(-move_speed)  # Move left
    if keys[pygame.K_RIGHT]:
        motorx.move(move_speed)   # Move right


    # Move Motory vertically
    if keys[pygame.K_UP]:
        motory.move(-move_speed)  # Move up
    if keys[pygame.K_DOWN]:
        motory.move(move_speed)   # Move down

    # Ensure Motory always has the same x coordinate as Motor
    motory.x = motorx.x    

    win.fill(WHITE)
    # Blit the sudoku image onto the window
    win.blit(sudoku_img, (100, 100))

    motorx.draw(win)
    motory.draw(win)
    
    # Update the display
    pygame.display.update()

pygame.quit()
