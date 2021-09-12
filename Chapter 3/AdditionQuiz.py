import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

answer = eval(input(f"What is {number1} + {number2} ? "))

correctAnswer = number1 + number2
print(f"The correct answer is {correctAnswer}")
if answer == correctAnswer:
    print("Congrats! Maths genius!")
else:
    print("Sorry, you are wrong...")