def handConvert(cards):
    card_rank = {
         '2': 0,
         '3': 1,
         '4': 2,
         '5': 3,
         '6': 4,
         '7': 5,
         '8': 6,
         '9': 7,
         'T': 8,
         'J': 9,
         'Q': 10,
         'K': 11,
         'A': 12
    }
    card_suit ={
         'C': 0,
         'D': 1,
         'H': 2,
         'S': 3
    }
    result = []
    for card in cards:
        result.append([card_rank[card[0]],card_suit[card[1]]])
    result.sort()
    result.reverse()
    return result


def check_royal(cards):
    if(cards[0][0]==12):
        if cards[0][0]-1 == cards[1][0] and cards[0][1] == cards[1][1]:
            if cards[1][0]-1 == cards[2][0] and cards[1][1] == cards[2][1]:
                if cards[2][0]-1 == cards[3][0] and cards[2][1] == cards[3][1]:
                    if cards[3][0]-1 == cards[4][0] and cards[3][1] == cards[4][1]:
                        return True
    return False

def check_straightFlush(cards):
    if cards[0][0]-1 == cards[1][0] and cards[0][1] == cards[1][1]:
        if cards[1][0]-1 == cards[2][0] and cards[1][1] == cards[2][1]:
            if cards[2][0]-1 == cards[3][0] and cards[2][1] == cards[3][1]:
                if cards[3][0]-1 == cards[4][0] and cards[3][1] == cards[4][1]:
                    return cards[0][0]
    return False   

def check_fourOfKind(cards):
    cardRanks = [cards[0][0],cards[1][0],cards[2][0],cards[3][0],cards[4][0]]
    for cardRank in cardRanks:
        if (cardRanks.count(cardRank)==4):
            return cardRank
    return False

def check_fullHouse(cards):
    if(check_threeOfKind(cards) and check_onePair(cards)):
        return True
    return False

def check_flush(cards):
    cardSuits = [cards[0][1],cards[1][1],cards[2][1],cards[3][1],cards[4][1]]
    for cardSuit in cardSuits:
        if(cardSuits.count(cardSuit)==5):
            return cards[0][0]          
    return False

def check_straight(cards):
    if cards[0][0]-1 == cards[1][0]:
        if cards[1][0]-1 == cards[2][0]:
            if cards[2][0]-1 == cards[3][0]:
                if cards[3][0]-1 == cards[4][0]:
                    return cards[0][0]
    return False    

def check_threeOfKind(cards):
    cardRanks = [cards[0][0],cards[1][0],cards[2][0],cards[3][0],cards[4][0]]
    for cardRank in cardRanks:
        if (cardRanks.count(cardRank)==3):
            return cardRank
    return False

def check_twoPair(cards):
    cardRanks = [cards[0][0],cards[1][0],cards[2][0],cards[3][0],cards[4][0]]
    pairRank =[]
    pairs=0
    for cardRank in cardRanks:
        if (cardRanks.count(cardRank)==2):
            pairRank.append(cardRank)
            pairs+=1
            cardRanks.remove(cardRank)
    pairRank.sort()
    if(pairs==2):
        return pairRank[0]
    return False

def check_onePair(cards):
    cardRanks = [cards[0][0],cards[1][0],cards[2][0],cards[3][0],cards[4][0]]
    for cardRank in cardRanks:
        if (cardRanks.count(cardRank)==2):
            return cardRank
    return False
    
def highCard(cards):
    return cards[0][0]

def main():
    ties=0
    p1=0
    p2=0
    with open(r'./poker.txt', 'r') as f:
        for line in f:
            cards_p1 = []
            cards_p2 = []
            line = line.strip().split(' ')

            if line[-2:-1] == '\n':
                line = line[:-2]
            
            cards_p1 = line[:5]
            cards_p2 = line[5:]

            res1 = handConvert(cards_p1)
            res2 = handConvert(cards_p2)

            if check_royal(res1)==True and check_royal(res2)==True:
                    ties+=1
            elif check_royal(res1)==True and check_royal(res2)==False:
                p1+=1
            elif check_royal(res2)==True and check_royal(res1)==False:
                p2+=1

            elif check_straightFlush(res1) and check_straightFlush(res2):
                if check_straight(res1)>check_straightFlush(res2):
                    p1+=1
                elif check_straight(res2)>check_straightFlush(res1):
                    p2+=1
            elif check_straightFlush(res1) and check_straightFlush(res2)==False:
                p1+=1
            elif check_straightFlush(res1)==False and check_straightFlush(res2):
                p2+=1


            elif check_fourOfKind(res1) and check_fourOfKind(res2):
                if check_fourOfKind(res1)>check_fourOfKind(res2):
                    p1+=1
                elif check_fourOfKind(res2)>check_fourOfKind(res1):
                    p2+=1
            elif check_fourOfKind(res1) and check_fourOfKind(res2)==False:
                p1+=1
            elif check_fourOfKind(res1)==False and check_fourOfKind(res2):
                p2+=1

            elif check_fullHouse(res1) and check_fullHouse(res2):
                if check_threeOfKind(res1)>check_threeOfKind(res2):
                    p1+=1
                elif check_threeOfKind(res2)>check_threeOfKind(res1):
                    p2+=1
                if check_onePair(res1)>check_onePair(res2):
                    p1+=1
                elif check_onePair(res1)<check_onePair(res2):
                    p2+=1

            elif check_fullHouse(res1) and check_fullHouse(res2)==False:
                p1+=1
            elif check_fullHouse(res1)==False and check_fullHouse(res2):
                p2+=1            

            elif check_flush(res1) and check_flush(res2):
                if check_flush(res1)>check_flush(res2):
                    p1+=1
                elif check_flush(res2)>check_flush(res1):
                    p2+=1
                        
            elif check_flush(res1) and check_flush(res2)==False:
                p1+=1
            elif check_flush(res1)==False and check_flush(res2):
                p2+=1   

            elif check_straight(res1) and check_straight(res2):
                if check_straight(res1)>check_straight(res2):
                    p1+=1
                elif check_straight(res2)>check_straight(res1):
                    p2+=1
            elif check_straight(res1) and check_straight(res2)==False:
                p1+=1
            elif check_straight(res1)==False and check_straight(res2):
                p2+=1   

            elif check_threeOfKind(res1) and check_threeOfKind(res2):
                if check_threeOfKind(res1)>check_threeOfKind(res2):
                    p1+=1
                elif check_threeOfKind(res2)>check_threeOfKind(res1):
                    p2+=1
                
            elif check_threeOfKind(res1) and check_threeOfKind(res2)==False:
                p1+=1
            elif check_threeOfKind(res1)==False and check_threeOfKind(res2):
                p2+=1 

            elif check_twoPair(res1) and check_twoPair(res2):
                if check_twoPair(res1)>check_twoPair(res2):
                    p1+=1
                elif check_twoPair(res2)>check_twoPair(res1):
                    p2+=1
                
            elif check_twoPair(res1) and check_twoPair(res2)==False:
                p1+=1
            elif check_twoPair(res1)==False and check_twoPair(res2):
                p2+=1 

            elif check_onePair(res1) and check_onePair(res2):
                if check_onePair(res1)>check_onePair(res2):
                    p1+=1
                elif check_onePair(res2)>check_onePair(res1):
                    p2+=1
            elif check_onePair(res1) and check_onePair(res2)==False:
                p1+=1
            elif check_onePair(res1)==False and check_onePair(res2):
                p2+=1
            elif highCard(res1)>highCard(res2):
                p1+=1
            elif highCard(res2)>highCard(res1):
                p2+=1

    print(f"Player 1 : {p1} wins")
if __name__ == '__main__':
    main()