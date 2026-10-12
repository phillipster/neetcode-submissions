class Solution:
    def checkValidString(self, s: str) -> bool:
        parens, stars = [], []
        for i, c in enumerate(s):
            if c == '(':
                parens.append(i)
            elif c == '*':
                stars.append(i)
            else:  # c == ')'
                if not parens and not stars:
                    return False
                if parens:
                    parens.pop()
                else:
                    stars.pop()
        while parens and stars:
            if parens.pop() > stars.pop():
                return False
        return not parens