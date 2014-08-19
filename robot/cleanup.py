from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here def line(dir):
def turner(dir):
  dir = dir*-1
  turn(dir)
  move()
  turn(dir)

def go(dir):
  while touch() is fruit
    move()
  
  if dir ==1:
    while left_side() is fruit
      move()

  if dir ==-1:
    while right_side is fruit
      move()
  turner(dir)  
    


dir = 1
go(dir)


