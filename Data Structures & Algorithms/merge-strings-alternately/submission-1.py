class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        m, n = len(word1), len(word2)
        i = j = 0
        while i < m and j < n:
            if i <= j:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
        res += word1[i:]
        res += word2[j:]
        # while i < m:
        #     res.append(word1[i])
        #     i += 1
        # while j < n:
        #     res.append(word2[j])
        #     j += 1
        return ''.join(res)