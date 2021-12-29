import random


def a() -> float:
    success: int = 0
    cases: int = 0
    for _ in range(100000):
        x: float = random.uniform(-10, 10)
        y: float = random.uniform(0, 10)
        if (0 <= x <= 10 and 0 <= y <= 10) and (x ** 2 + y ** 2 <= 100):
            success += 1
        if x ** 2 + y ** 2 <= 100:
            cases += 1
    return success / cases


def b() -> float:
    success: int = 0
    cases: int = 0
    for _ in range(100000):
        x: float = random.uniform(-10, 10)
        y: float = random.uniform(0, 10)
        if x ** 2 + y ** 2 <= 25:
            success += 1
        if x ** 2 + y ** 2 <= 100:
            cases += 1
    return success / cases


def c() -> float:
    return 1 - b()


def d() -> float:
    success: int = 0
    cases: int = 0
    for _ in range(100000):
        x: float = random.uniform(-10, 10)
        y: float = random.uniform(0, 10)
        if x ** 2 + ((y - 5) ** 2) <= 25:
            success += 1
        if x ** 2 + y ** 2 <= 100:
            cases += 1
    return success / cases


if __name__ == "__main__":
    print('it lands in the right half of the target: ', a())
    print('its distance from the center is less than 5 inches: ', b())
    print('its distance from the center is greater than 5 inches: ', c())
    print('it lands within 5 inches of the point (0, 5): ', d())
