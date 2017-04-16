import sys, pygame

from Engine.updateable import IUpdateable

pygame.font.init()
defaultfont = pygame.font.SysFont("comicsansms",30)

class FrameLabel(IUpdateable):
    def __init__(self, color = (255, 0, 0), font = defaultfont):
        super().__init__()
        self.color = color;
        self.font = font
        self.framerate = 0
    
    def update(self, clock):
        self.framerate = str(round(clock.get_fps(),0))
        
    def draw(self, screen):
        label = self.font.render(self.framerate, 1, self.color)
        rect = screen.blit(label, (screen.get_width() - self.font.size(self.framerate)[0]-5, 0))