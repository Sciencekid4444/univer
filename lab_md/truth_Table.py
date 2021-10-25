def truthTable_generator(expression,nlen):
    variables = []
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    expression.lower()
    for ch in alfabet:
        x=expression.find(ch)
        if x!=-1:
            nlen=nlen+1
            variables.append(ch)
            alfabet.remove(ch)
    
    expression=expression.replace('*','and')
    expression=expression.replace('+','or')
    expression=expression.replace('!','not ')
    if nlen==2:
        print("-------------")
        print("| X | Y | " + expression + " ")
        print("-------------")
        for x in range(0,2):
            for y in range(0,2):
                result = eval(expression)
                result = 1 if result==True or result==1 else 0            
                print('| '+str(x)+' | '+str(y)+' | ' + str(result) +' ')
                print("-------------")

    if nlen==3:
        print("-----------------")
        print("| X | Y | Z | " + expression + " ")
        print("-----------------")
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    result = eval(expression)
                    result = 1 if result==True or result==1 else 0
                    print('| '+str(x)+' | '+str(y)+' | '+str(z)+' | ' + str(result) +' |')
                    print("-----------------")

    if nlen==4:
        print("---------------------")
        print("| X | Y | Z | K | " + expression + " ")
        print("---------------------")
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    for k in range(0,2):
                        result = eval(expression)
                        result = 1 if result==True or result==1 else 0
                        print('| '+str(x)+' | '+str(y)+' | '+str(z)+' | '+str(k)+' | ' + str(result) +' ')
                        print("---------------------")



expression = input()
truthTable_generator(expression,1)      