import pygame

from Engine.updateable import IUpdateable

class Game(IUpdateable):
    def __init__(self):
        self.objects = list()
    
    def update(self, clock):
        for object in self.objects:
            object.update(clock)
        
    def draw(self, screen):
        for object in self.objects:
            object.draw(screen)
            
    def addObject(self, Gameobject):
        self.objects.append(Gameobject)
    
    def removeObject(self,Gameobject):
        self.objects.remove(Gameobject)