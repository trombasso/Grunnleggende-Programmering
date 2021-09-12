import random

loop_until_quit = True
while loop_until_quit:

    lottery = str(random.randint(0, 9)) + str(random.randint(0, 9))
    guess = input("Enter your lottery pick (two digits): ")
    if int(guess) > 99:
        print("Error, wrong number.")    
        exit()
    else:
        print("The lottery number is", lottery)
        if guess == lottery:
            print("Exact match: you win $10,000")
        elif guess[1] == lottery[0] and guess[0] == lottery[1]:
            print("Match all digits: you win $3,000")
        elif guess[0] == lottery[0] or guess[0] == lottery[1] \
                or guess[1] == lottery[0] or guess[1] == lottery[1]:
            print("Match one digit: you win $1,000")
        else:
            print("Sorry, no match")
            
    loop = input("Would you like to try again (y/n)? ")
    if loop == "y":
        loop_until_quit = True
    else:
        loop_until_quit = False