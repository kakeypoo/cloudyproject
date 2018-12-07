import pygame as pg
import sys

pg.init()

#window
win = pg.display.set_mode((1000, 1000))
win.fill((0, 0, 0))
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

  def create(self, win):
    cook = pg.transform.scale(self.__pic, (self.__w, self.__h))
    win.blit(cook, (self.__x, self.__y))
  def get_x(self):
    return self.__x
  def get_vel(self):
    return self.__vel
  
class Food:
  def __init__(self, pic, x, y, w, h):
    self.__x = x #blitting
    self.__y = y
    self.__w = w #transforming
    self.__h = h
    self.__pic = pic
    
  def create(self, win):
    food = pg.transform.scale(self.__pic, (self.__w, self.__h))
    win.blit(food, (self.__x, self.__y))
                              
    
XVAL = 200
YVAL = 400
VELVAL = 8

run = True
while run:
  
  cook = Player(COOK, XVAL, YVAL, 50, 50, VELVAL)
  bacon = Food(BACON, 200, 600, 50, 50)
  donut = Food(DONUT, 200, 500, 50, 50)
  fries = Food(FRIES, 200, 450, 50, 50)
  hotdog = Food(HOTDOG, 200, 300, 50, 50)
  icecream = Food(ICECREAM, 200, 200, 50, 50)
  pizza = Food(PIZZA, 200, 100, 50, 50)
  popcorn = Food(POPCORN, 200, 600, 50, 50)
  apple = Food(APPLE, 300, 600, 50, 50)
  avocado = Food(AVOCADO, 400, 600, 50, 50)
  broccoli = Food(BROCCOLI, 500, 600, 50, 50)
  carrot = Food(CARROT, 200, 600, 50, 50)
  pineapple = Food(PINEAPPLE, 700, 600, 50, 50)
  strawberry = Food(STRAWBERRY, 800, 600, 50, 50)
  watermelon = Food(WATERMELON, 900, 600, 50, 50)


  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False
      pg.quit()
      sys.exit()

  keys = pg.key.get_pressed()
  if keys[pg.K_RIGHT]:
    if XVAL < 1000 - 50 - 8:
      XVAL += VELVAL
  elif keys[pg.K_LEFT]:
    if XVAL > VELVAL:
      XVAL -= VELVAL

  win.fill((0,0,0))
  
  cook.create(win)
  bacon.create(win)
  donut.create(win)
  fries.create(win)

  pg.display.flip()
