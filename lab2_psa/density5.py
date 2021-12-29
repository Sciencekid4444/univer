import random

# coin is 1 unit long
# the coin to be within it has to land in middle
# and not on edges, thus 4 possible positions
square: list = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]


def simulate() -> float:
    success: int = 0
    for _ in range(10000):
        x: int = random.randint(0, 3)
        y: int = random.randint(0, 3)

        if square[x][y] == 1:
            success += 1
    return success / 10000


if __name__ == "__main__":
    print(simulate())
