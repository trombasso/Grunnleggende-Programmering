import random


def dice_roll():
    a = random.randint(1, 6)
    b = random.randint(1, 6)

    return a + b


def main():
    score_board = {x: 0 for x in range(2, 13)}
    for x in range(1000):
        dice_total = dice_roll()
        score_board[dice_total] += 1

    print("Total Simulated Expected")
    print("   Percent Percent")
    for x in range(2, 13):
        print(f"{x}   {(score_board[x] / 1000)*100:.2f}   {x-1/36:.2f}")


if __name__ == "__main__":
    main()
