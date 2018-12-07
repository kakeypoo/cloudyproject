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
##  def getpic(self):
##    return self.__pic
##  def getx(self):
##    return self.__x
##  def gety(self):
##    return self.__y
##  def getw(self):
##    return self.__w
##  def geth(self):
##    return self.__h
##  def getvel(self):
##    return self.__vel
  
  def draw(self, win):
    cook = pg.transform.scale(self.__pic, (self.__w, self.__h))
    win.blit(cook, (self.__x, self.__y))
  
class Food:
  def __init__(self, pic, x, y, w, h):
    self.__x = x #blitting
    self.__y = y
    self.__w = w #transforming
    self.__h = h
    self.__pic = pic
    
  def draw(self, win):
    food = pg.transform.scale(self.__pic, (self.__w, self.__h))
    win.blit(food, (self.__x, self.__y))
                              
#accessors 
##  def getfoodx(self):
##    return self.__x
##  def getfoody(self):
##    return self.__y
##  def getfoodw(self):
##    return self.__w
##  def getfoodh(self):
##    return self.__h
##  def getfoodpic(self):
##    return self.__pic

cook = Player(COOK, 200, 400, 50, 50, 8)
bacon = Food(BACON, 200, 600, 50, 50)

run = True
while run:
  cook.draw(win)
  bacon.draw(win)
  
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()

  pg.display.flip()



    
    
