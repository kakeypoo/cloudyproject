from pygame import *

class Sprite():

  def __init__(self, x, y, speed):
    #image
    self.__sprite_image = pygame.image.load('cook.png')
    
    #location
    self.__sprite_x = x
    self.__sprite_y = y
    
    #size
    self.__width = 50 #placeholder
    self.__height = 70

    #how fast it moves across screen
    self.__speed = speed
  
  #mutators
  def go_left(self):
    self.__sprite_x -= self.__speed
  def go_right(self):
    self.__sprite_y += self.__speed

  #accessors
  def locx_sprite(self):
      return self.__sprite_x
  def locy_sprite(self):
      return self._sprite_y
  
    

class Screen():

  def __init__(self, x, y, text):
    self.__x_val = x
    self.__y_val = y
    self.__background = 
    self.__text = text
    
  #Accessors  
  def limit_x(self):
    return self.__x_val
  def limit_y(self):
    return self.__y_val
  
  

  

  
  
    
