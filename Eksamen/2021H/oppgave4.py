def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def isPrimeReversed(number):
    temp = number
    revers = 0

    while number > 0:
        dig = number % 10
        revers = revers * 10 + dig
        number = number // 10
    if temp == revers:
        return True


if __name__ == "__main__":
    reversed_numbers = 0
    number = 1
    while reversed_numbers < 20:
        if isPrime(number):
            if isPrimeReversed(number):
                print(number, end=" ")
                reversed_numbers += 1
                if reversed_numbers % 5 == 0:
                    print()
        number += 1
