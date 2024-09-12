import pygame as pg

from event_container import EventContainer
from main_window import MainWindow

class App():
    def __init__(self):
        self.__init()
        self.__is_running = True
        self.__event_container = EventContainer()
        self.max_fps = 60
        self.clock = pg.time.Clock()
        self.window = MainWindow()


    def update(self):
        self.window.update() 
        self.__event_container.process_event()       

    def subscribeEvent(self, e: int, func: callable):
        self.__event_container.add_event(e, func)

    @property
    def run(self, value: bool):
        self.__is_running = value

    def __init(self):
        pg.init()

    def main_loop(self):
        while self.__is_running:
            self.update()
            self.clock.tick()
            