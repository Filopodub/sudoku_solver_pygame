import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) 

class Pen:
    def __init__(self, x, y):
        """Initializes the pen at the same x and y position as Motor and Motory."""
        self.x = x
        self.y = y
        self.radius = 5
        self.active = False

    def toggle_active(self):
        """Toggles the pen's active state when the spacebar is pressed."""
        self.active = not self.active
        self.radius = 15 if self.active else 5  # Change radius when active

    def draw(self, win):
        """Draws the pen as a circle with the current radius."""
        pygame.draw.circle(win, RED, (self.x, self.y), self.radius)

    def update_position(self, x, y):
        """Updates the position of the pen to match Motor and Motory."""
        self.x = x
        self.y = y

    def read(self, surface):
        """Reads the color at the current pen position on the given surface (sudoku image area)."""
        color = surface.get_at((self.x, self.y))[:3]  # Get the RGB value of the pixel
        if color == WHITE:
            return 0  # White
        elif color == BLACK:
            return 1  # Black
        else:
            return -1  # For colors other than white or black