# Recursive version of dec2bin
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end="")


if __name__ == "__main__":

    dec_val = int(input("Enter a number: "))
    DecimalToBinary(dec_val)
    print("\nFinished!")
