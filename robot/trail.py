from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def tri():
  move()
  a =str(touch())
  l=str(left_side())
  r=str(right_side())
  if l=='fruit':
    return -1
  elif r=='fruit':
    return 1
  else:
    print 'oh no im stuck'
    return(0)
for i in range (0,400):
  a =str(touch())
  l=str(left_side())
  r=str(right_side())
  if a =='fruit':
    move()
  elif r=='fruit':
    turn (1)
    move()
  elif l=='fruit':
    turn(-1)
    move()
  else:
    turn(tri())
    move()
  