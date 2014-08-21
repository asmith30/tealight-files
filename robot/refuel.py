from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
for i in range(0,400):
  a=str(touch())
  l=str(left_side())
  r=str(right_side())
  if l=="None"orl=='fruit':
    turn(-1)
  elif a=='wall':
    turn(1)
  move()
