
import pygame as pg

from app import App

app = App()
app.subscribeEvent(pg.QUIT, lambda: pg.quit())
app.main_loop()



    
