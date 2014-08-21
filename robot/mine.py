from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
flip =0
turn(1)
for i in range (1,500):
  a = str(touch())
  l=str(left_side())
  r=str(right_side())
  lasta ='fruit'
  lastl='fruit'
  lastr='fruit'
  print i
  if a=='wall':
    uturn()
  if a=='fruit':
    lasta='fruit'
  elif l=='fruit':
    if r=='fruit':
      turn(flip*2-1)
      flip=(flip + 1)%2
    else:
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
  
  def uturn():
    if l=='fruit':
      turn(-1)
      move()
      turn(-1)
    else:
      turn(1)
      move()
      turn(1)
    
