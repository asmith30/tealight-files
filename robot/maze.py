from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
import random

# Add your code here:

for i in range(0,300):
  a = touch()
  l = left_side()
  r = right_side()
  '''
  print str(a) + ' ' + str(r) +' ' + str(l) 
  '''
  if ((str(a) == 'None') and (str(r) == 'None') and (str(l)== 'None')) :
    #print 'three way'
    turn(random.randint(-1,1))
    move()
  if str(a)=='None' and str(r) == 'None' and str(l) == 'wall' :
    #print 'ahead and right'
    turn(random.randint(0,1))
    move()
  if str(a)== 'none' and str(r) == 'wall' and str(l) ==  'None':
    print 'ahead and left'
    turn (random.randint(-1,0))
    move()
  if str(a) == 'None' and str(r) =='wall' and str(l) ==  'wall':
    #print 'ahead only'
    move()
  if str(a) == 'wall' and str(r) == 'None' and str(l) == 'None' :
    #print 'left and right only'
    turn (random.randint(0,1)*2-1)
    move()
  if str(a) == 'wall' and str(r) == 'None' and str(l) == 'wall' :
    #print 'right only'
    turn(1)
    move()
  if str(a) == 'wall' and str(r) == 'wall' and str(l) == 'None' :
    #print'left only'
    turn(-1)
    move()
  if str(a) == 'wall' and str(r) == 'wall' and str(l) == 'wall' :
    #print 'dead end'
    turn(2)
    move()
       

  