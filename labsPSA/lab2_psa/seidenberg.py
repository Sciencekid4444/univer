import random as rnd
import matplotlib.pyplot as plt

probability: list = []
rolls: list = []


def solution() -> list:
    for i in range(5, 15, 1):
        winnings: int = 0
        rolls.append(i)
        for _ in range(0, 10000):
            score: int = 0
            throws: int = 0
            while score <= 14 and throws <= i:
                throws += 1
                dice1: int = rnd.randint(1, 6)
                dice2: int = rnd.randint(1, 6)
                dice3: int = rnd.randint(1, 6)
                score = dice1 + dice2 + dice3
                if score == 14:
                    winnings += 1
        probability.append(winnings / 10000)
    return probability


def main() -> any:
    print(solution())
    plt.scatter(rolls, probability, label="Seidenberg", color="green",
                marker=".")
    plt.xlabel('x - rolls')
    plt.ylabel('y - P(x)')
    plt.title('Seidenberg')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
