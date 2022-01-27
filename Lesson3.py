import pygame
import random
#-----------------Create a circle at X,Y--------------------------------------------------------
def createcircle(x,y):
  circle={}
  circle["color"]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  circle["x"]=x #random.randint(0,255)
  circle["y"]=y #random.randint(0,255)
  circle["speedx"]= random.randint(-100,100)/100
  circle["speedy"]= random.randint(-100,100)/100
  circle["noise"]= 0.9 #random.randint(0,255)
  circle["shrink"] = 0.99  # random.randint(0,255)
  circle["gravity"] = 0.001
  circle["size"]=10#random.randint(10,100)
  return circle
#------------------Draw a circle--------------------------------------------------------
def drawcircle(circle):
    circle["x"]+=circle["speedx"]+random.randint(-1,1)*circle["noise"]
    circle["y"]+=circle["speedy"]+random.randint(-1,1)*circle["noise"]
    circle["speedy"]+=circle["gravity"]
    circle["size"]*= circle["shrink"]
    pygame.draw.circle(screen, circle["color"], [int(circle["x"]),int(circle["y"])], int(circle["size"]))
#----------------initiate pygame---------------------------------------------------------
pygame.init()
screensize=500
screen=pygame.display.set_mode([screensize,screensize])
objs=[]
#----------------------------Main loop--------------------------------------------------------------------
for i in range(1000000):
  pygame.event.get()
  x,y = pygame.mouse.get_pos() # Get position of the mouse
  obj = createcircle(x, y)
  objs.append(obj)
  pygame.Surface.fill(screen,(0,0,0))
  for ob in objs:
       drawcircle(ob)
  pygame.display.update()
