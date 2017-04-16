import pygame

class IUpdateable():
    def __init__(self):
        pass
    
    def update(self, clock):
        raise NotImplementedError()
        
    def draw(self, screen):
        raise NotImplementedError()