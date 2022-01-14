import turtle

x1 = float(input("Enter X-coordinate for Point 1: "))
y1 = float(input("Enter Y-coordinate for Point 1: "))

x2 = float(input("Enter X-coordinate for Point 2: "))
y2 = float(input("Enter Y-coordinate for Point 2: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("The distance between the two objects is", distance)

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1", font=("Times", 12))
turtle.goto(x2, y2)
turtle.write("Point 2", font=("Times", 12))

turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance, font=("Times", 12))

turtle.done()