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
  if touch() == 'None':
    if right_side() == 'None':
      if left_side() == 'None':
        turn(random.randint(-1,1))
        move()
      else:
        turn(random.randint(0,1))
        move()
    elif left_side() =='None':
      turn (random.randint(-1,0))
      move()
    else:
      move()
  elif right_side() =='None':
    if left_side() =='None':
      turn (random.randint(0,1)*2-1)
      move()
    else:
      turn(1)
      move()
  else:
    turn(-1)
    move()
    
       

  