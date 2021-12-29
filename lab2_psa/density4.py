import math
import random


def get_roots(b: float, c: float) -> tuple:
    d: float = b ** 2 - 4 * c
    if d >= 0:
        d = math.sqrt(d)
        root1: float = (-b - d) / 2
        root2: float = (-b + d) / 2
        return root1, root2
    return False, False


def simulate_real() -> float:
    success: int = 0
    for _ in range(10000):
        b: float = random.uniform(-1, 1)
        c: float = random.uniform(-1, 1)

        roots: tuple = get_roots(b, c)
        if roots[0] and roots[1]:
            success += 1
    return success / 10000


def simulate_positive() -> float:
    success: int = 0
    for _ in range(10000):
        b: float = random.uniform(-1, 1)
        c: float = random.uniform(-1, 1)

        roots: tuple = get_roots(b, c)
        if roots[0] > 0 and roots[1] > 0:
            success += 1
    return success / 10000


if __name__ == "__main__":
    print('real solutions', simulate_real())
    print('positive solutions:', simulate_positive())
