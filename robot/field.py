from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
'''
algorithm to find 
if smell is 1 then try touch, left right and move there
if smell is 2 do a spiral search until found, then retest

'''
def bomb():
  if touch() == 'fruit':
    move()
  elif left_side() == 'fruit':
    turn(-1)
    move()
  elif right_side() == 'fruit':
    turn(1)
    move()

'''
try a spiral pattern
'''
def spiral():
  for i in range (2,3):
    for j in range (1,i):
     move()
    turn (-1)
    bomb()
    for j in range (1,i):
      move()
    turn(-1)
    bomb()
    
for i in range(0,5):
  print smell()
  move ()
  bomb()

