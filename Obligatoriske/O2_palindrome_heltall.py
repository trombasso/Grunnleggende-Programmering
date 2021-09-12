def is_palindrome(user_input):
    input_list = list(user_input)
    input_list_reversed = list(user_input)
    input_list_reversed.reverse()
    if input_list_reversed == input_list:
        return True
    else:
        return False


def main():
    print("\nPalindromechecker 2.0")
    user_input = input("Enter string to check: ")
    # user_input = input("Enter string to check: ").lower   # !! This does not work, why?
    if is_palindrome(user_input) is True:
        print(f"\nYes, <{user_input}> is a palindrome!\n")
    else:
        print(f"\nSorry, <{user_input}> is not a palindrome\n")


if __name__ == "__main__":
    main()
    print("hehe")
