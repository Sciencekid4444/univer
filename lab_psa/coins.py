from random import randint
total_earnings = []
N= 1000000
def sums(arr):
    sum=0
    for elem in arr:
        sum+=elem
    return sum

def winnings():
    for i in range(N):
        sum=0
        flipped = 1   
        while(sum==0):
         if (randint(1,2)==2):
            sum = 2**flipped
         else:
          flipped+=1
        total_earnings.append(sum)

    total = sums(total_earnings)
    return total/N

def main():
    res = winnings()
    print(res)

if __name__ == '__main__':
    main()