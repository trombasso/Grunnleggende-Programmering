import turtle
import random

t = turtle.Turtle()

n=10
while n <= 40:
    t.color("red")
    t.circle(n)
    n = n + 10
    
turtle.Screen().exitonclick()