from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def ur():
  turn(-1)
  move()
  turn(1)
  move()
  
def dr():
  turn(1)
  move()
  turn(-1)
  move()
def ul():
  print 'default'
  
def trythisway():
  move()
  if left_side()=='fruit':
    return -1
  elif right_side()=='fruit':
   return 1
  else:
     turn(2)
     move()
     return(0)
  
def find():
  while touch()!='fruit' and left_side()!='fruit' and right_side()!='fruit':
   if look()=='fruit':
      move()
   else:
      turn(-1)
  move()
  
def traverse():
  d = trythisway()
  if d<>0:
    turn(d)
    move()
    turn(d*-1)
  else:
    traverse()
    
  
find()  
for i in range(0,400):
  a=str(touch())
  l=str(left_side())
  r=str(right_side())
  print look()
  print smell()
  print touch()
  move()