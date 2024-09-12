import pygame as pg

class Window():
    def __init__(self, size: pg.Vector2):
        self.__init()
        self.size = size
        self.screen = pg.display.set_mode(size)
    
    def __init(self):
        pg.display.init()

    def update(self):
        pg.display.update()