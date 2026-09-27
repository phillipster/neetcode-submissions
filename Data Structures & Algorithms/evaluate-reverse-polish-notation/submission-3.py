class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = "+-*/"
        for t in tokens:
            if t not in operators:
                s.append(t)
            else:
                n2, n1 = int(s.pop()), int(s.pop())
                if t == '+':
                    s.append(n1 + n2)
                elif t == '-':
                    s.append(n1 - n2)
                elif t == '*':
                    s.append(n1 * n2)
                else:
                    s.append(n1 / n2)
        return int(s[0])