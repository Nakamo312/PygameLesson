import pygame as pg

class EventContainer():
    def __init__(self):
        self.__events: dict[int, callable] = dict()
    
    def add_event(self, e: int, func: callable):
        self.__events[e] = func
    
    def process_event(self):
        for e in self.__events:
            self.__events[e]()
