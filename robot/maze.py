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
  a = touch()
  l = left_side()
  r = right_side()
  print a+r+l  
  if ((a == 'None') and (r == 'None') and (l == 'None')) :
    print 'three way'
    turn(random.randint(-1,1))
    move()
  if a=='None' and r == 'None' and l == 'wall' :
    print 'ahead and right'
    turn(random.randint(0,1))
    move()
  if a== 'none' and r == 'wall' and l ==  'None':
    print 'ahead and left'
    turn (random.randint(-1,0))
    move()
  if a == 'None' and r =='wall' and l ==  'wall':
    print 'ahead only'
    move()
  if a == 'wall' and r == 'None' and l == 'None' :
    print 'left and right only'
    turn (random.randint(0,1)*2-1)
    move()
  if a == 'wall' and r == 'None' and l == 'wall' :
    print 'right only'
    turn(1)
    move()
  if a == 'wall' and r == 'wall' and l == 'None' :
    print'left only'
    turn(-1)
    move()
  if a == 'wall' and r == 'wall' and l == 'wall' :
    print 'dead end'
    turn(2)
    move()
       

  