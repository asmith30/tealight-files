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
def snaker():
  line()
  small(1)
  line()
  small(-1)
  
 

snaker()
