from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

#
def scan():
  i = 0
  while look()=='wall' and i<4:
    turn()
    i=i+1
  if look()=='wall':
    return 0
  else:
    return 1
for i in range (0,400)
  found = scan()
  while found == 0:
    move()
    found = scan()
  while touch()=='None':
    move()
  if touch()=='fruit'
  move()