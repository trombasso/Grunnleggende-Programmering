char_str = input("Input a string of characters: ")
if len(char_str) == 0:
    print("Input has to be more than zero characters...")
    exit()

consecutive_chars = 0
currentcount = 1
totalcount = 1
theletter = char_str[0]

for char in range(0, len(char_str) - 1):
    if char_str[char] == char_str[char + 1]:
        currentcount += 1
    else:
        currentcount = 1

    if currentcount > totalcount:
        totalcount = currentcount
        theletter = char_str[char]

print(
    f"The number of consecutive repeating characters is {totalcount}, the letter is '{theletter}'. "
)
