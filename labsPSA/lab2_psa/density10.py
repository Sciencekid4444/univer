from random import randint


if __name__ == "__main__":
    list1: list = [0]
    for i in range(0, 19):
        list1.append(1)
    list2: list = [0]
    for i in range(0, 49):
        list2.append(1)

    total: int = 0
    offences: int = 0

    for k in range(10000):
        for i in range(730):
            index2: int = randint(0, 49)
            if list2[index2] == 0:
                total += 2
            else:
                index1: int = randint(0, 19)
                if list1[index1] == 0:
                    offences += 1
                    if offences == 0:
                        total += 50
                    elif offences == 1:
                        total += 150
                    else:
                        total += 300

    print(f'Total offences: {offences / 10000}')
    print(f'Total spent by Jora: {total / 10000} lei')
    print(f'Total spent by Student: {365 * 4} lei')
