class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        total = 0
        for op in operations:
            print(op, s)
            if op == 'C':
                total -= s.pop()
            elif op == '+':
                s.append(s[-1] + s[-2])
                total += s[-1]
            elif op == 'D':
                s.append(s[-1]*2)
                total += s[-1]
            else:
                s.append(int(op))
                total += s[-1]
        return total