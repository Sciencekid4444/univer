from random import randint

N = 100000


def empty(revolver):
    for idx in range(len(revolver)):
        revolver[idx]=0

def load(revolver,adjacent):
    empty(revolver)
    if(adjacent):
        rand = randint(0, len(revolver) - 1)
        if rand != len(revolver) - 1:
            revolver[rand] = revolver[rand + 1] = 1
        else:
            revolver[0] = revolver[-1] = 1
    else:
        bulletSlot = randint(0,len(revolver)-1)
        bulletSlot2 = randint(0,len(revolver)-1)
        revolver[bulletSlot]=1
        while(bulletSlot2==bulletSlot or bulletSlot2+1==bulletSlot or bulletSlot2-1==bulletSlot):
            bulletSlot2 = randint(0,len(revolver)-1)
        revolver[bulletSlot]=revolver[bulletSlot2]=1

def respin(revolver,adjacent):
    alive=0
    for _ in range(N):
        empty(revolver)
        load(revolver,adjacent)
        rand = randint(0,len(revolver)-1)
        if(revolver[rand]==0):
            alive+=1
    return 100-((N - alive)/N * 100)

def stay(revolver,adjacent):
    alive=0
    for _ in range(N):
        load(revolver,adjacent)
        rand = randint(0,len(revolver)-1)
        while revolver[rand]!=0:
            rand=randint(0,len(revolver)-1)
        if rand-1 < 0:
            if revolver[len(revolver)-1]==0:
                alive+=1
        elif revolver[rand-1]==0:
                alive+=1
    return 100-((N-alive)/N*100)


def main():
    revolver = [0,0,0,0,0,0]
    r = respin(revolver,True)
    print(f'6 slots adjacent w re-spin chance of survival {r}%')
    s = stay(revolver,True)
    print(f'6 slots adjacent w no-spin chance of survival {s}%')
    r = respin(revolver,False)
    print(f'6 slots w respin chance of survival {r}%')
    s = stay(revolver,False)
    print(f'6 slots w no-spin chance of survival {s}%')
    revolver = [0,0,0,0,0]
    r = respin(revolver,True)
    print(f'\n\n5 slots adjacent w respin chance of survival {r}%')
    s = stay(revolver,True)
    print(f'5 slots  adjacent w no-spin chance of survival {s}%')
    r = respin(revolver,False)
    print(f'5 slots w respin chance of survival {r}%')
    s = stay(revolver,False)
    print(f'5 slots w no-spin chance of survival {s}%')

if __name__ == '__main__':
    main()
