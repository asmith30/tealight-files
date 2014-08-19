from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def line():
  for i in range (0,32)
    move()
# function to do line row line row
def snaker():
  line()
  turn(1)
  move(4)
  turn(1)
  line()
  turn(-1)
  move(4)
  turn(-1)

snaker()
