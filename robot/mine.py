from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
for i in range (1,400):
  a = str(touch())
  l=str(left_side())
  r=str(right_side())
  lasta ='fruit'
  lastl='fruit'
  lastr='fruit'

  if a=='fruit':
    elif l=='fruit':
    turn(-1)
    elif r=='fruit':
    turn(1)
  else:
    turn(2)
  move()
