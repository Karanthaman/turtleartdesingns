import turtle
from instruct import *
sam = turtle.Turtle()
bob = turtle.Turtle()
jake = turtle.Turtle()
turtle.tracer(0)

turtle.bgcolor("black")
jake.reset()
jake.hideturtle()
jake.speed(0)
jake.color("white")
for p in range(500):
    jake.forward(p)
    jake.left(120)
    
sam.reset()
sam.hideturtle()
sam.speed(0)
sam.color("blue")
for i in range(1000):
  sam.forward(i)
  sam.right(98)

bob.reset()
bob.hideturtle()
bob.speed(0)
bob.color("red")
for l in range(500):
    bob.forward(l)
    bob.left(40)


