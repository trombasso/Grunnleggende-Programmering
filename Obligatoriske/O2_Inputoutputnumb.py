def numfilter(numbers):
    numlist_a = numbers.split()
    numlist_b = []

    for elem in numlist_a:
        # ignore
        if elem == " ":
            continue
        elif elem in numlist_b:
            continue
        elif elem not in numlist_b:
            numlist_b.append(elem)

    print("\nRaw-input:")
    for elem in numlist_a:
        print(elem, end=" ")

    print("\nFiltered-output:")

    for elem in numlist_b:
        print(elem, end=" ")

    print("\n")


def main():
    numfilter(input("\nPlease input integers with space between (i.e. 4 5 33 33 7 8 8): "))


if __name__ == "__main__":
    main()
