import pygame
class Button:
    def __init__(self, text, x, y, size):
        self.x = x+10
        self.y = y+10
        self.text = text
        self.font = pygame.font.SysFont("Helvetica",size)
        self.hovered = False
        self.border = 3
        self.width = 0
        self.height = 0
        

    def draw(self, screen, mouse_position):
        render = self.font.render(self.text,False,(250,250,250))
        self.width = render.get_width() + 20
        self.height = render.get_height() + 20

        self.checkHover(mouse_position)
        if self.hovered:
            self.border = 0
        else:
            self.border = 3
        
        pygame.draw.rect(screen,(50,50,50), pygame.Rect(self.x - 10, self.y - 10, self.width, self.height), self.border)
        screen.blit(render,(self.x, self.y))

    def checkHover(self, mouse_position):
        if (mouse_position[0] > self.x - 10 and mouse_position[1] > self.y - 10 and mouse_position[0] < self.x - 10 +  self.width  and mouse_position[1] < self.y - 10 + self.height ):
            self.hovered = True
            return True
        else:
            self.hovered = False
            return False
    