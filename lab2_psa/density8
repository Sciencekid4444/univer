import random
import matplotlib.pyplot as plt

winnings: list = []
x_values: list = []


def simulate() -> float:
    for _ in range(10000):
        x: float = random.uniform(0, 1)
        y: float = random.uniform(0, 1)
        i: int = 1
        while y <= x:
            i += 1
            y = random.uniform(0, 1)
        winnings.append(i - 1)
        x_values.append(x)


simulate()
plt.plot(x_values, winnings)
plt.show()
