from random import randint
total_earnings_player = []
total_earnings_bank = []

N = 100000
def sums(arr):
    sum = 0
    for elem in arr:
        sum += elem
    return sum

def winnings(fee):
    for i in range(N):
        game = 0
        flipped = 1
        while game == 0:
          if randint(1, 2) == 2:
            game = 2**flipped
          else:
            flipped += 1
        sum_player = game - fee
        total_earnings_player.append(sum_player)

    player = sums(total_earnings_player)/N
    print(f'Player money: ', player)

def main():
    for i in range(10):
        print(f'fee : {i}', winnings(i))
        print()
if __name__ == '__main__':
    main()