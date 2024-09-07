import pygame
import os


WIDTH, HEIGHT = 50, 50
MOTOR_IMG = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "motor.png")), (WIDTH, HEIGHT))
BLUE = (0, 0, 255)

class Motorx:
    IMG = MOTOR_IMG
    Y = 50
    MINX, MAXX  = 50, 450

    def __init__(self):
        """Initializes the base with a starting vertical position (y-coordinate)."""
        self.y = self.Y  
        self.x = 50  

    def draw(self, win):
        start_pos = (self.MINX, self.Y )    
        end_pos = (self.MAXX, self.Y )      
        line_thickness = 5       
        pygame.draw.line(win, BLUE, start_pos, end_pos, line_thickness)
        win.blit(self.IMG, (self.x - WIDTH/2, self.y - HEIGHT/2))

    def move(self, dis):
        self.x += dis
        if self.x < self.MINX:
            self.x = self.MINX
        elif self.x > self.MAXX:
            self.x = self.MAXX


        