def truthtable(n):
      if n < 1:
        return [[]]
      subtable = truthtable(n-1)
      return [ row + [v] for row in subtable for v in [0,1] ]

def printPowerSet( set ):
    tt = truthtable(len(set))
    print('[',end='')
    for subtt in tt:
        print('[',end='')   
        for idx in range(0,len(subtt)):
            if subtt[idx]==1:
                print(f'{ set[idx]} ',end ="")
        if tt[len(tt) - 1]==subtt:
            print("]",end='')
        else:
            print("]",end='')
    print(']')
    print(tt)
set = [[],1,[2],3,4]

printPowerSet(set)
