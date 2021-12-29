class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        for i in range(0, len(p) - 1):
            if (i + 1 < len(p)) and p[i].isalpha() and p[i + 1] == '*':
                if p[i] not in s:
                    p = p[:i] + p[i + 2:]
        if not s and p:
            for i in range(0, len(p) - 1):
                if i + 1 < len(p) and (p[i] == '.' or p[i].isalpha()) and p[i] == '*':
                    p = p[:i] + p[i + 2:]
                else:
                    p = p[:i] + p[i + 1:]
        if not s and (not p or p == '.'):
            return True
        elif s and not p:
            return False
        elif not s and p:
            return False

        # case by case recursion
        if len(p) == 2 and p[0] == '.' and p[1] == '*':
            return True
        elif len(p) >= 3 and p[0] == '.' and p[1] == '*':
            expChar = s[0]
            while len(s) > 0 and s[0] == expChar:
                s = s[1:]
            p = p[2:]
            return self.isMatch(s, p)

        elif len(p) >= 2 and p[1] == "*":
            patternChar = p[0]
            p = p[2:]
            while len(s) > 0 and s[0] == patternChar and p != s:
                s = s[1:]
            return self.isMatch(s, p)

        elif p[0] == '.':
            p = p[1:]
            s = s[1:]
            return self.isMatch(s, p)

        elif p[0].isalpha():
            if s[0] == p[0]:
                s = s[1:]
                p = p[1:]
                return self.isMatch(s, p)
            else:
                return False

a = Solution()
s = 'ab'
p = '.*..'
print(a.isMatch(s,p))