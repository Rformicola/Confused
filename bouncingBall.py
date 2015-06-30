import pygame

pygame.init()

red = 255,0,0
blue = 0,0,255
white = 255,255,255

x,y = 400,200
bounce = False

window = pygame.display.set_mode((800,600))
pygame.display.set_caption('This is a random file')

stop = False 

while not stop:

  window.fill(white)
  
  pygame.draw.Circle(window, red, (x,y), 10))
  pygame.draw.line(window, blue, (0,500),(800,500),4)
  
  y += 5
  
  if y + 10 == 500:
    bounce = True
    
  if bounce:
    y -= 5 
    
  if y - 10 == 200:
    bounce = False
    
  pygame.display.update()
    
  
  

