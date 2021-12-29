from random import randint
import matplotlib.pyplot as plt


def list_randomizer(lst):
    l = lst[::]
    rand_list = []
    length = len(l)
    counter = length - 1
    for _ in range(length):
        rand_index = randint(0, counter)
        rand_list.append(l[rand_index])
        l.remove(l[rand_index])
        counter -= 1
    return rand_list


def pair_maker(lst):
    length = len(lst)
    pairs = []
    for i in range(length):
        current = []
        current.append(lst[i])
        current.append(lst[i - 1])
        current.sort()
        pairs.append(current)
    return pairs


people = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

percentages: list = []
tables: list = []
for j in range(19):
    success: int = 10000
    tables.append(j)
    for counter in range(10000):
        temp: int = 0
        morning_table = list_randomizer(people)
        evening_table = list_randomizer(people)

        morning_pairs = pair_maker(morning_table)
        evening_pairs = pair_maker(evening_table)
        for pair in morning_pairs:
            if temp:
                continue
            if pair in evening_pairs:
                success -= 1
                temp = 1

    # print(success)
    length: int = len(people)
    percentage = success / 10000
    percentages.append(percentage)
    print(percentage)
    for z in range(5):
        people.append(people[-1] + 1)

plt.plot(tables, percentages)
plt.show()
