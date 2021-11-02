def match(expression, pattern):
    exp = expression
    pat = pattern
    print(exp,pat)
    if not exp and not pat:
        return True
    elif exp and not pat:
        return False
    elif not exp and pat:
        return False

    if len(pat) >= 3 and pat[0] == '.' and pat[1] == '*' and pat[2].isalpha():
        pat = pat[2:]
        while exp[0] != pat[0]:
            exp = exp[1:]
        if exp and pat:
            p = pat[1:]
            pat = p
        return match(exp, pat)
    elif len(pat) == 2 and pat[0] == '.' and pat[1] == '*':
        return True
    elif len(pat) >= 2 and pat[1] == '*':
        t = pat[0]
        pat = pat[2:]
        if t == '.':
            while len(exp)>0:
                exp = exp[1:]
            return match(exp,pat)
        if t == exp[0]:
            while len(exp) > 0 and exp[0] == t:
                exp = exp[1:]
            return match(exp, pat)
        return match(exp, pat)

    elif pat[0] == '.':
        pat = pat[1:]
        exp = exp[1:]
        return match(exp, pat)
    elif pat[0].isalpha():
        if exp[0] == pat[0]:
            while exp != "" and pat != "" and exp[0] == pat[0]:
                if len(pat) > 1 and (pat[1] == '*' or pat[1] == '.'):
                    break
                exp = exp[1:]
                pat = pat[1:]
            return match(exp, pat)
        else:
            return False





expression = str(input())
pattern = str(input())
print(match(expression, pattern))
