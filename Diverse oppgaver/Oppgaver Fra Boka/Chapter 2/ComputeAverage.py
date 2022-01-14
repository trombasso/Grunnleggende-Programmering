print("Please enter three numbers:")
one = float(input("1: "))
two = float(input("2: "))
three = float(input("3: "))

solution = (one + two + three) / 3
# print("The average of " + str(one) + ", " + str(two) + " and "  + str(three) + " is: " + str(solution) +".")
# print("The average of ", one, ", ", two, " and ", three, " is: ", solution,".")
print(f"The average of {one}, {two} and {three} is {solution:0.2f}.")
