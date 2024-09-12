import pygame as pg
import logging


class GameObject():  
    counter = 0  

    def __init__(self, parent : "GameObject" = None, id: str = None):
        self.id = id if id else f"GameObject{GameObject.counter}"
        GameObject.counter += 1
        self.parent = parent
        self.children: dict[str, GameObject] = dict()
    
    
    def recouursive(self):
        def wrapper(self):
            ...
        for id in self.children:
            self.children[id].recouursive()
        return wrapper
    
    
    def __del__(self):
        if len(self.children) != 0:
            for id in self.children:
                self.remove_child(id)

    def add_child(self, id: str, obj: "GameObject"):
        i = 0
        while id in self.children:
            id = f"{id}{i}"
            i += 1
        
        self.children[id] = obj

    def remove_child(self, id: str):
        if id in self.children:
            del self.children[id]
    

    @recouursive
    def update(self):
        ...

    def draw(screen: pg.Surface):
        ...