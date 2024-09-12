import pygame as pg

class MainWindow():
    def __init__(self):
        self.__init()
        self.background_color = pg.Color(255,255,255)
        self.size_screen = pg.Vector2(500,500)
        self.screen = pg.display.set_mode(self.size_screen)

    def update(self):
        self.screen.fill(self.background_color)
        pg.display.update()
    
    def __init(self):
        pg.display.init()
    
    def set_caption(self, caption: str):
        pg.display.set_caption(caption)
