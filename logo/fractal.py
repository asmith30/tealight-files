from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    segment(scale / 3.0, detail - 1)
    turn(-75)
    segment(scale / 3.0, detail - 1)
    turn(150)
    segment(scale / 3.0, detail - 1)
    turn(-75)
    segment(scale / 3.0, detail - 1)
    

turn(90)
move(-300)
segment(600,6)
move(-300)