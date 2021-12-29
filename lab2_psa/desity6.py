import random
import matplotlib.pyplot as plt

tosses: list = []
heads: list = []

if __name__ == "__main__":
    for i in range(10000):
        head: int = 0
        while head < 35 or head > 75:
            head = 0
            for j in range(100):
                if random.randint(0, 1):
                    head += 1
        heads.append(head)

    plt.hist(heads, bins=100)
    plt.show()
