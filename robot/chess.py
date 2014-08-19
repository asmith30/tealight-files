from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def line():
  for i in range (0,32):
    move()
def small(dir):
  turn(dir)
  for i in range (0,4):
    move()
  turn(dir)
  
# function to do line row line row
def snaker(dir):
  line()
  small(dir)
  line()
  small(dir*-1)
  
def side(dir): 
  for i in range (0,4):
    snaker(dir)

side(1)
turn(-1)
side(-1)