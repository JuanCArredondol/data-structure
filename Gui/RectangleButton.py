import pygame
class RectangleButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hovered = False
        self.border = 3
        self.width = 65
        self.height =65
        self.selected = False

    def draw(self, screen, mouse_position):

        self.checkHover(mouse_position)
        if self.selected:
            self.border = 0
        else:
            self.border = 3
        pygame.draw.rect(screen,(0,255,0), pygame.Rect(self.x , self.y, self.width, self.height),self.border)
        pygame.draw.rect(screen, (0,255, 0),  pygame.Rect(self.x+10 , self.y+10, self.width-20, self.height-20), self.border)

    def checkHover(self, mouse_position):
        if (mouse_position[0] > self.x  and mouse_position[1] > self.y  and mouse_position[0] < self.x +  self.width  and mouse_position[1] < self.y + self.height ):
            return True
        else:
            return False
    
    def setClick(self):
        if self.selected:
            self.selected = False
        else:
            self.selected = True    

    def setFalse(self):
        self.selected = False