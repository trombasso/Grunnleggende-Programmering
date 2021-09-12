import random
from os import system, name
from time import sleep

operator = ["", "+", "-", "*", "/"]

correct_answer = 0
wrong_answer = 0


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
            print(
                f"\nYou had {correct_answer} correct answers and {wrong_answer} wrong answers.\n"
            )
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
    global wrong_answer
    global correct_answer
    while True:
        selection = menu()
        number_one = random.randint(1, 10)
        number_two = random.randint(1, 10)
        if selection == "2" or "4":
            if number_two > number_one:
                (number_two, number_one) = (number_one, number_two)

        question = float(
            input(f"\nWhat is {number_one} {operator[selection]} {number_two} = ")
        )
        answer = calculation(number_one, operator[selection], number_two)

        if answer == question:
            correct_answer += 1
            print("------------------------------------------------------")
            print("That is correct!")
            print("------------------------------------------------------")

        elif answer != question:
            wrong_answer += 1
            print("------------------------------------------------------")
            print(f"Sorry, the correct answer is {answer} Try again!")
            print("------------------------------------------------------\n")

        sleep(2)


if __name__ == "__main__":
    main()
