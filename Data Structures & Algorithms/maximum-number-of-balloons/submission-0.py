class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = defaultdict(int)
        for letter in text:
            m[letter] += 1
        numTimes = 0
        while True:
            for letter in "balloon":
                if m[letter] < 1:
                    return numTimes
                m[letter] -= 1
            numTimes += 1