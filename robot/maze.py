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
 
 
  if ((a == 'None')& (r == 'None') &(l == 'None')) :
    print 'three way'
    turn(random.randint(-1,1))
    move()
  if a=='None' & r == 'None' & l == 'wall' :
    print 'ahead and right'
    turn(random.randint(0,1))
    move()
  if a== 'none' & r == 'wall' & l ==  'None':
    print 'ahead and left'
    turn (random.randint(-1,0))
    move()
  if a == 'None' & r =='wall' & l ==  'wall':
    print 'ahead only'
    move()
  if a == 'wall' & r == 'None' & l == 'None' :
    print 'left and right only'
    turn (random.randint(0,1)*2-1)
    move()
  if a == 'wall' & r == 'None' & l == 'wall' :
    print 'right only'
    turn(1)
    move()
  if a == 'wall' & r == 'wall' & l == 'None' :
    print'left only'
    turn(-1)
    move()
  if a == 'wall' & r == 'wall' & l == 'wall' :
    print 'dead end'
    turn(2)
    move()
       

  