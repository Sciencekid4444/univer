import random


def boarding() -> bool:
    people: int = 100
    taken_seats: list = [False for _ in range(0, 100)]
    passengers: list = []
    # -1 means hasn't boarded yet
    for idx in range(0, 100):
        passengers.append({'person': idx, 'ticket_seat': idx, 'current_seat': -1})
    for idx in range(0, 100):
        if idx == 0:
            new_seat: int = random.randint(0, 99)
            passengers[idx]['current_seat'] = new_seat
            taken_seats[new_seat] = True
        else:
            if not taken_seats[idx]:
                correct_seat: int = passengers[idx]['ticket_seat']
                passengers[idx]['current_seat'] = correct_seat
                taken_seats[correct_seat] = True
            else:
                has_seat: bool = False
                while not has_seat:
                    new_seat: int = random.randint(0, 99)
                    if not taken_seats[new_seat]:
                        passengers[idx]['current_seat'] = new_seat
                        has_seat = True
                        taken_seats[new_seat] = True

    return passengers[people - 1]['current_seat'] == passengers[people - 1]['ticket_seat']


def simulate() -> float:
    success: int = 0
    for _ in range(10000):
        if boarding():
            success += 1
    return success / 10000


print(simulate())
