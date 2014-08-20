from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here def line(dir):
def turner(dir):
  turn(dir)
  move()
  turn(dir)

def go(dir):
  while touch() != 'fruit':
  move()
  while touch() == 'fruit':
    move()
  if dir == 1:
    while left_side() == 'fruit':
      move()
  if dir == -1:
    while right_side() == 'fruit':
      move()
  dir =dir*-1    
  turner(dir)  
    


dir = 1
for i in range(0,500):
  go(dir)
  dir = dir*-1
  print dir


