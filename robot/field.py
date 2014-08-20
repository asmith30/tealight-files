from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def spiral():
  for i in range (1,40):
    for j in range (1,i):
     move()
    turn (-1)
    for j in range (1,i):
      move()
    turn(-1)
    
for i in range(0,15):
  print smell()
  move ()
spiral()