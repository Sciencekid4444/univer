import random


def simulate() -> float:
    success: int = 0
    for _ in range(10000):
        if random.randint(1, 100) == 1:
            success += 1
    return success / 10000


print(simulate() * 1000)
