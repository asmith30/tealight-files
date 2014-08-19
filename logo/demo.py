from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "yellow", "blue"]

for i in range(100,500):
  move(i)
  turn(99)
  color(colors[i%3])