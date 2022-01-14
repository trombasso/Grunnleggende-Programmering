def bin2dec(binary_number):
    # binary_number = input("Enter binary number: ")

    answer = 0
    x = len(binary_number) - 1
    i = 0

    for elem in range(0, len(binary_number)):
        binary_int = int(binary_number[i])
        answer += binary_int * (2 ** (x - i))

        i += 1

    return answer


def main():
    binary = input("Enter binary string: ")
    print(bin2dec(binary))


if __name__ == "__main__":
    main()
