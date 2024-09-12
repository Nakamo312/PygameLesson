import pygame as pg

from game_object import GameObject

class Scene():
    def __init__(self):
        self.objects: list[GameObject] = []

    def add(self, object: GameObject):
        self.objects.append(object)
    
    def update(self):
        for obj in self.objects:
            obj.update()
    
    def draw(self, screen: pg.Surface):
        for obj in self.objects:
            obj.draw(screen) 