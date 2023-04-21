import pygame
class CircleButton:
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
        pygame.draw.rect(screen,(0,0,255), pygame.Rect(self.x , self.y, self.width, self.height), self.border)
        pygame.draw.circle(screen, (0, 0, 255),(((self.x+(self.x+self.width))/2),((self.y+(self.y+self.height))/2)), 25, 3)

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

    