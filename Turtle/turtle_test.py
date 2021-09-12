import turtle

#Constants
TARGET_LLEFT_X = 50
TARGET_LLEFT_Y = 50
TARGET_RIGHT = 150
TARGET_WIDTH = 100
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
EAST = 0
WEST = 180
NORTH = 90
SOUTH = 270
FORCE_FACTOR = 30

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.hideturtle()

#Draw target
turtle.penup()
turtle.goto(TARGET_LLEFT_Y, TARGET_LLEFT_X)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()
turtle.goto(0,0)

# Ask user for unput
angle = float(input("Angi vinkel: "))
force = float(input("Angi kraft(1-10): "))

#Distance
distance = FORCE_FACTOR * force

turtle.setheading(angle)
turtle.pendown()
turtle.forward(distance)
turtle.showturtle()

#Hit the target?
xcor = turtle.xcor
ycor = turtle.ycor
if(turtle.xcor() >= TARGET_LLEFT_X) and \
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and \
        turtle.ycor() >= TARGET_LLEFT_Y and \
            turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH):
                print("You hit the target!")
else:
    print("U missed")
turtle.done()
turtle.exitonclick