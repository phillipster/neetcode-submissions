class WordDictionary:

    def __init__(self):
        self.data = {}

    def addWord(self, word: str) -> None:
        cur = self.data
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur[None] = None

    def search(self, word: str) -> bool:
        def helper(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c != ".":
                    if c not in cur:
                        return False
                    cur = cur[c]
                else:
                    for letter in cur:
                        if letter is not None and helper(i + 1, cur[letter]):
                            return True
                    return False
            return cur and None in cur

        return helper(0, self.data)

                        
        