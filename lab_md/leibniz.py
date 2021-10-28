def leibniz(size):
    result = [[0 for rows in range(size + 1)] for cols in range(size + 1)]
    i = 0
    while (i <= size):
        j = 0
        while (j <= i):
            if (j == i or j == 0):
                result[i][j] = 1
            else:
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
            j += 1
        i += 1
    i = 1
    while (i <= size):
        j = i
        while (j < size):
            print("\t", end="")
            j += 1

        j = 1
        while (j <= i):
            if (i == 1 and j == 1):
                print("1".center(8),end='')
            else:
                r = str('1/' + str(result[i - 1][j - 1] * i)).center(8)
                print(r,end='')

            j += 1

        print()
        i += 1
        
def main():
    leibniz(5)
if __name__ == '__main__':
    main()