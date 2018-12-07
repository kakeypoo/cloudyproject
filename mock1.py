import pygame as pg
import sys

pg.init()

#window
win = pg.display.set_mode((1000, 1000))
#constants
COOK = pg.image.load('cook.png')
BACON = pg.image.load('Bbacon.png')
DONUT = pg.image.load('Bdonut.png')
FRIES = pg.image.load('Bfries.png')
HOTDOG = pg.image.load('Bhotdog.png')
ICECREAM = pg.image.load('Bicecream.png')
PIZZA = pg.image.load('Bpizza.png')
POPCORN = pg.image.load('Bpopcorn.png')
APPLE = pg.image.load('apple.png')
AVOCADO = pg.image.load('avocado.png')
BROCCOLI = pg.image.load('broccoli.png')
CARROT = pg.image.load('carrot.png')
PINEAPPLE = pg.image.load('pineapple.png')
STRAWBERRY = pg.image.load('strawberry.png')
WATERMELON  = pg.image.load('watermelon.png')

clock = pg.time.Clock()
FPS = 40

class Player:
  def __init__(self, pic, x, y, w, h, vel): #x, y position w, h transform scale
    self.__x = x #blitting
    self.__y = y
    self.__w = w #transforming
    self.__h = h
    self.__vel = vel 
    self.__pic = pic

class Food:
  def __init__(self, pic, x, y, w, h):
    self.__x = x
    self.__y = y
    self.__w = w
    self.__h = h
    self.__pic = pic





    
    
