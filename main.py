#turtle party project 



import turtle
turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
  
def suqare(size):
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)
    
suqare(100)
back(125)
suqare(50)
