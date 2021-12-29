import numpy as np
import math


def equationroots(a: int, b: float, c: int) -> tuple:
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    if dis > 0:
        root1: float = (-b + sqrt_val) / (2 * a)
        root2: float = (-b - sqrt_val) / (2 * a)
        return root1, root2
    return False, False


def simulate() -> float:
    success: int = 0
    for _ in range(10000):
        u: float = np.random.uniform(0, 1)
        r1, r2 = equationroots(1, 4 * u, 1)
        if r1 and r2:
            success += 1
    return success / 10000


if __name__ == "__main__":
    print(simulate())
