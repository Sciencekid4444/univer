expression = input()
dictionary ={}
vars = []
for i in range(0,len(expression)):
    if expression[i].isalpha():
        if expression[i] not in dictionary:
            dictionary[expression[i]] = 0
            vars.append(expression[i])
t = 0
for var in vars:
    print(f'{var}|', end='')
    t += 1
print(expression)

expression = expression.replace('*', 'or')
expression = expression.replace('+', 'and')
expression = expression.replace('!', 'not ')
arr = [0]*(len(dictionary))
for i in range(0, 2**len(dictionary)):
    for j in range(0, len(dictionary)):
        val = (i & (1 << j))
        if val > 0:
            val = 1
        # print(val,end='')
        arr[j] = val
    k = 0
    for key in dictionary:
        dictionary[key] = arr[k]
        k += 1
    for elem in arr:
        print(elem, end="|")
    print(eval(expression,None,dictionary))