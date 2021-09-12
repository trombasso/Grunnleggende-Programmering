import random
from os import system, name
from time import sleep

operator = ["", "+", "-", "*", "/"]


def clear():
    if name == "nt":  # for windows
        _ = system("cls")
    else:  # for mac and linux
        _ = system("clear")


def menu():
    inputcheck = False
    while inputcheck is False:
        clear()
        print("------------------------------------------------------")
        print("Main Menu:")
        print("------------------------------------------------------")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Exit")
        print("------------------------------------------------------")
        selection = int(input("Enter choice: "))
        if selection == 5:
            exit()
        elif selection in range(1, 5):
            inputcheck = True
            return selection
        else:
            print("\nNot a valid option")
            sleep(1)


def calculation(number_one, operator, number_two):
    if operator == "+":
        answer = number_one + number_two
    elif operator == "-":
        answer = number_one - number_two
    elif operator == "*":
        answer = number_one * number_two
    elif operator == "/":
        answer = number_one / number_two

    return answer


def main():
    while True:
        selection = menu()
        number_one = random.randint(1, 10)
        number_two = random.randint(1, 10)
        if selection == "2":
            if number_two > number_one:
                (number_two, number_one) = (number_one, number_two)

        question = float(
            input(f"\nWhat is {number_one} {operator[selection]} {number_two} = ")
        )
        answer = calculation(number_one, operator[selection], number_two)

        if answer == question:
            print("------------------------------------------------------")
            print("That is correct!")
            print("------------------------------------------------------")

        elif answer != question:
            print("------------------------------------------------------")
            print(f"Sorry, the correct answer is {answer} Try again!")
            print("------------------------------------------------------\n")

        sleep(2)


if __name__ == "__main__":
    main()
