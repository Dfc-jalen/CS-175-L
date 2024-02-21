#Jalen Smith
#Cs 175-L
#Mr. Eckert


import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
LENGTH = 100
ANGLE = 45

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

screen = turtle.Screen()
screen.setup(WINDOW_WIDTH,WINDOW_HEIGHT)
screen.bgcolor("white")

turtle.color("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(-40,-80)
turtle.pendown()
for i in range(8):
  turtle.width(8)
  turtle.forward(LENGTH)
  turtle.left(ANGLE)
  
  turtle.begin_fill()
turtle.penup()
turtle.goto(-30,-55)
turtle.pendown()
for i in range(8): 
  turtle.forward(80)
  turtle.left(ANGLE)
turtle.end_fill()

turtle.end_fill()
turtle.penup()
turtle.goto(-55,10)
turtle.end_fill()
turtle.color("white")
turtle.end_fill()
'''It's funny because on replit(my main coding software), the font is the exact one
in the document, but for some reason it looks different on idle. I will send you a screenshot to show
you what I mean. (SINCE i know it has to be

"what the customer asked for" - Boss '''

turtle.write("STOP", font=("Comic Sans MS", 35, "bold"))
turtle.hideturtle()

screen.mainloop() 

             
  

             
  
