def xnor(x,y):
    if ((x and y)or(not x and not y))==True:
        return 1
    return 0

def main():
    print(xnor(0,0))
    print(xnor(0,1))
    print(xnor(1,0))
    print(xnor(1,1))

if __name__ == '__main__':
    main()