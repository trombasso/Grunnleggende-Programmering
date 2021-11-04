input_number = input("Legg inn et nummer mellom 0-1000: ")

# if input_number == 1000:
#     print("1")
# else:
#     c = input_number % 10
#     inputShortened = input_number // 10
#     b = inputShortened % 10
#     a = inputShortened // 10
#     print(a + b + c)


digits = []

for digit in input_number:
    digits.append(int(input_number))

print(sum(digits))
