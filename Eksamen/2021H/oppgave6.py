def valid_password(value):
    charupper = False
    length = False
    charlower = False
    number = False

    if len(value) > 7:
        length = True
    for char in value:
        if char.isupper():
            charupper = True
    for char in value:
        if char.islower():
            charlower = True
    for char in value:
        if (
            char == "1"
            or char == "2"
            or char == "3"
            or char == "4"
            or char == "5"
            or char == "6"
            or char == "7"
            or char == "8"
            or char == "9"
        ):
            number = True

    if (charupper != True) or (charlower != True) or (length != True) or (number != True):
        return False

    return True


def main():
    password = valid_password(input("Enter Password: "))
    if password:
        print("Valid Password!")
    else:
        print("Not a valid password!")


if __name__ == "__main__":
    main()
