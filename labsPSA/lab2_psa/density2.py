import random


def simulate() -> float:
    init_stick: int = 10
    success: int = 0
    for _ in range(10000):
        break_point: int = random.randint(1, init_stick - 1)
        stick1: int = init_stick - break_point
        if break_point < stick1:
            temp: int = stick1
            stick1 = break_point
            break_point = temp

        stick3: int = random.randint(1, break_point - 1)
        stick2: int = break_point - stick3

        if stick2 + stick3 > stick1:
            success += 1
    return success / 10000


if __name__ == "__main__":
    print(simulate())
# always will return 1 bcs we divide the first stick into two ones,
# and the bigger one again so always 2 sticks coming from the bigger side will be bigger than initial
