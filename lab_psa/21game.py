from random import randint


def game(n,k,maxpts):
    N = 100000
    res=0
    for _ in range(N):
        start=0
        while(start<k):
            rand = randint(1,maxpts)
            start += rand
        if(start<=n):
            res+=1
    return (res/N)
        
def main():
    n = 10
    k = 1
    maxpts = 10

    res = game(n, k, maxpts)
    print(res)

if __name__ == '__main__':
    main()