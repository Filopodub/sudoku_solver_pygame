import pygame
import os


WIDTH, HEIGHT = 50, 50
MOTOR_IMG = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "motor.png")), (WIDTH, HEIGHT))
BLUE = (0, 0, 255)


class Motory:
    IMG = MOTOR_IMG
    X = 50
    MINY, MAXY = 50, 450

    def __init__(self, x):
        """Initializes the motory with a starting x position from Motor and a y position."""
        self.y = 50
        self.x = x  # X coordinate will match Motor's x

    def draw(self, win):
        start_pos = (self.x, self.MINY)    
        end_pos = (self.x, self.MAXY)      
        line_thickness = 5       
        pygame.draw.line(win, BLUE, start_pos, end_pos, line_thickness)
        win.blit(self.IMG, (self.x - WIDTH/2, self.y - HEIGHT/2))

    def move(self, dis):
        """Move the motory vertically, ensuring it stays within bounds."""
        self.y += dis
        if self.y < self.MINY:
            self.y = self.MINY
        elif self.y > self.MAXY:
            self.y = self.MAXY