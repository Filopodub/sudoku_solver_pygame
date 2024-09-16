import pygame
from motorx import Motorx
from motory import Motory
from pen import Pen

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
pen = Pen(motorx.x, motory.y)

# Movement speed
move_speed = 1

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pen.toggle_active()  # Toggle pen activation on spacebar press
        
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

    # Update Pen's position to match MotorX and Motory
    pen.update_position(motorx.x, motory.y)

    # Fill the window with white before drawing
    win.fill(WHITE)  

    # Read the color at the pen's position and print it
    win.blit(sudoku_img, (100, 100))
    pen_color = pen.read(win)
    print(f"Color: {'White' if pen_color == 0 else 'Black' if pen_color == 1 else 'Other'}")
    
    # Draw everything
    motorx.draw(win)
    motory.draw(win)
    pen.draw(win)

        
    # Update the display
    pygame.display.update()

pygame.quit()
