import math
import random


def get_coordinates(R: int) -> tuple:
    r = R * math.sqrt(random.uniform(0, 1))
    theta = random.uniform(0, 1) * 2 * math.pi
    length = math.sqrt(random.uniform(0, 1)) * r
    return length * math.cos(theta), length * math.sin(theta)


def get_length(t1: tuple, t2: tuple) -> float:
    t1_len: float = math.sqrt(t1[0] * t1[0] + t1[1] * t1[1])
    t2_len: float = math.sqrt(t2[0] * t2[0] + t2[1] * t2[1])
    return t1_len * t2_len


def get_dotProduct(t1: tuple, t2: tuple) -> float:
    return t1[0] * t2[0] + t1[1] * t2[1]


def get_angle(t1: tuple, t2: tuple, t3: tuple) -> float:
    t1t2: tuple = t2[0] - t1[0], t2[1] - t1[1]
    t1t3: tuple = t3[0] - t1[0], t3[1] - t1[1]
    t2t3: tuple = t3[0] - t2[0], t3[1] - t2[1]

    dot_product: float = get_dotProduct(t1t2, t1t3)
    length: float = get_length(t1t2, t1t3)
    theta: float = math.acos(dot_product / length)

    if math.degrees(theta) > 90:
        return False

    dot_product = get_dotProduct(t1t2, t1t3)
    length = get_length(t1t2, t1t3)
    theta = math.acos(dot_product / length)

    if math.degrees(theta) > 90:
        return False

    dot_product = get_dotProduct(t1t3, t2t3)
    length = get_length(t1t3, t2t3)
    theta = math.acos(dot_product / length)

    if math.degrees(theta) > 90:
        return False

    return True


def simulate() -> float:
    success: int = 0
    for _ in range(10000):
        t1: tuple = get_coordinates(5)
        t2: tuple = get_coordinates(5)
        t3: tuple = get_coordinates(5)

        if get_angle(t1, t2, t3):
            success += 1
    return success / 10000


if __name__ == "__main__":
    print(simulate())
