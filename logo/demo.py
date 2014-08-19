from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "yellow", "blue"]

for i in range(200,500):
  move(i)
  turn(93)
  color(colors[i%3])