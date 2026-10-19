class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        values = {letter : index for index, letter in enumerate(order)}
        print(values)
        for i in range(1, len(words)):
            prev, curr = words[i-1], words[i]
            print(prev, curr)
            m, n, i, j = len(prev), len(curr), 0, 0
            while i < m and j < n:
                if values[prev[i]] == values[curr[j]]:
                    i, j = i+1, j+1
                    continue
                if values[prev[i]] > values[curr[j]]:
                    return False
                else:
                    break
            if m > n and prev[n-1] == curr[n-1]:
                return False
        return True