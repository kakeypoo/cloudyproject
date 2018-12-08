import pygame as pg
import sys
import random

pg.init()

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

#TIME STUFF
clock = pg.time.Clock()
FPS = 40

#NUMBER CONSTANTS
#COOK
X_COORD = 500
Y_COORD = 977
FOOD_Y = -23

#SCREEN
WIDTH = 1000
HEIGHT = 1000

#ALL SPRITES
W = 46
H = 46
VELO = 8

FOODGROUP = pg.sprite.Group()

#window
win = pg.display.set_mode((WIDTH, HEIGHT))
win.fill((0, 0, 0))


'''CLASSES'''

class Sprite(pg.sprite.Sprite):
  def __init__(self, pic, x, y, w, h, vel, win):
    pg.sprite.Sprite.__init__(self)
    self.__image = pic
    self.__rect = self.__image.get_rect()
    self.__rect.center = [x, y] 
    self.__x = x
    self.__y = y
    self.__w = w
    self.__h = h
    self.__vel = vel
    self.__win = win
    
  def resize(self): #resizes 
    self.__image = pg.transform.scale(self.__image, (self.__w, self.__h))
 #   self.__win.blit(self.__image, (self.__x, self.__y))
  def move_player_left(self):
    if self.__x > self.__vel:
      self.__x -= self.__vel
      win.blit(self.__image, (self.__x, self.__y))
      pg.display.update()
      
  def move_player_right(self):
    if self.__x < WIDTH - self.__w - self.__vel:
      self.__y -= self.__vel
      win.blit(self.__image, (self.__x, self.__y))
      pg.display.update()
    
  def move_food(self):
    self.__rect.y += 2
    if self.__rect.top > 1000: 
      self.__rect.bottom = 0
      win.blit(self.__image, (self.__x, self.__y))
      pg.display.update()
 
##  def create(self, win): 
##    win.blit(self.__image, (self.__x, self.__y))
##    pg.display.update()
##    
##  def move_player_left(self):
##    if self.__x > self.__vel:
##      self.__x -= self.__vel
##      
##  def move_player_right(self):
##    if self.__x < WIDTH - self.__w - self.__vel:
##      self.__y -= self.__vel
##      
##  def move_food(self):
##    self.__rect.y += 2
##    if self.__rect.top > 1000: 
##      self.__rect.bottom = 0

   
##class Health:
##  def __init__(self):
##    self.__

    
#FUNCTIONS


def generate_x_val():
  x_start = random.randint(23, 977)
  return x_start
                       
def create_sprites():
  cook = Sprite(COOK, X_COORD, Y_COORD, W, H, VELO, win)
  
  #Use for loop add to list add to all sprites group
  bacon = Sprite(BACON, generate_x_val(), FOOD_Y, W, H, VELO, win)
  donut = Sprite(DONUT, generate_x_val(), FOOD_Y, W, H, VELO, win)
  fries = Sprite(FRIES, generate_x_val(), FOOD_Y, W, H, VELO, win)
  hotdog = Sprite(HOTDOG, generate_x_val(), FOOD_Y, W, H, VELO, win)
  icecream = Sprite(ICECREAM, generate_x_val(), FOOD_Y, W, H, VELO, win)
  pizza = Sprite(PIZZA, generate_x_val(), FOOD_Y, W, H, VELO, win)
  popcorn = Sprite(POPCORN, generate_x_val(), FOOD_Y, W, H, VELO, win)
  
  apple = Sprite(APPLE, generate_x_val(), FOOD_Y, W, H, VELO, win)
  avocado = Sprite(AVOCADO, generate_x_val(), FOOD_Y, W, H, VELO, win)
  broccoli = Sprite(BROCCOLI, generate_x_val(), FOOD_Y, W, H, VELO, win)
  carrot = Sprite(CARROT, generate_x_val(), FOOD_Y, W, H, VELO, win)
  pineapple = Sprite(PINEAPPLE, generate_x_val(), FOOD_Y, W, H, VELO, win)
  strawberry = Sprite(STRAWBERRY, generate_x_val(), FOOD_Y, W, H, VELO, win)
  watermelon = Sprite(WATERMELON, generate_x_val(), FOOD_Y, W, H, VELO, win)

  sprite_list = [cook, bacon, donut, fries, hotdog, icecream, pizza, popcorn, apple, \
               avocado, broccoli, carrot, pineapple, strawberry, watermelon]

  return sprite_list

def main():
  #MAIN LOOP
  run = True
  while run:

    for event in pg.event.get(): #DON't CHANGE
      if event.type == pg.QUIT:
        run = False
        pg.quit()
        sys.exit()
        
    food_list = create_sprites()
    #Key stuff
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT]:
      food_list[0].move_player_left()
      pg.display.update()
    elif keys[pg.K_RIGHT]:
      food_list[0].move_player_right()
      pg.display.update()
      
    win.fill((0, 0, 0))
    
    for food in food_list:
      food.resize()
 #     food.create(win)
      if not(food_list[0]):
        food.move_food()
      
    pg.display.flip()

main()
