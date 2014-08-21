from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
turn(1)
for i in range (1,400):
  a = str(touch())
  l=str(left_side())
  r=str(right_side())
  lasta ='fruit'
  lastl='fruit'
  lastr='fruit'
  
  if a=='fruit':
    print 'yay'
  elif l=='fruit':
    turn(-1)
  elif r=='fruit':
    turn(1)
  else:
    turn(1)
    if str(look())=='fruit':
      move()
    else:
      turn(2)
      if str(look())=='fruit':
        move()
      else:
        turn(1)
        for i in range(0,5):
          move()
  move()
