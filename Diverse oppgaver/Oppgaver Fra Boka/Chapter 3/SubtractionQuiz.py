import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

answer = int(input("What is " + str(number1) + " - " + str(number2) + "? "))
if number1 - number2 == answer:
    print("That's correct!")
else:
    print("Wrong answer :(")