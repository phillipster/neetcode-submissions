class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for symbol in s:
            if symbol not in counts:
                counts[symbol] = 1
            else:
                counts[symbol] += 1
        for symbol in t:
            if symbol not in counts:
                return False
            counts[symbol] -= 1
        for key in counts:
            if counts[key] != 0:
                return False
        return True