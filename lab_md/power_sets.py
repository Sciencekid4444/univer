from math import pow
def printPowerSet(set,set_size):
    print("[",end="")
    n=0
    powerSet_size = int(pow(2,set_size)) 
    for counter in range(0, powerSet_size):
        print("[ ",end="")               
        for j in range(0, set_size):
            if((counter & (1 << j)) > 0):
                print(set[j],end=" ")
        print("]",end=",")
        n += 1
    print("]")
    print(n)

#try:
#    set = []
#    while True:
#        set.append(int(input()))
#except:
#    printPowerSet(set, len(set))
set = [[],[1,2],1,2]

printPowerSet(set,len(set))