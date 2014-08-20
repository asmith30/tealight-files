from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
import random

# Add your code here:

for i in range(1,1500):
  print touch()
  if touch() == 'None':
    if right_side() == 'None':
      if left_side() == 'None':
        print 'three way'
        turn(random.randint(-1,1))
        move()
      else:
        print 'ahead and right'
        turn(random.randint(0,1))
        move()
    elif left_side() =='None':
      print 'ahead and left'
      turn (random.randint(-1,0))
      move()
    else:
      print 'ahead only'
      move()
  elif right_side() =='None':
    if left_side() =='None':
      print 'left and right only'
      turn (random.randint(0,1)*2-1)
      move()
    else:
      print 'right only'
      turn(1)
      move()
  else:
    print'left only'
    turn(-1)
    move()
    
       

  