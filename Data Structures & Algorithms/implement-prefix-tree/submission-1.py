class PrefixTree:
    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        cur = self.data
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur[None] = None
        

    def search(self, word: str) -> bool:
        cur = self.data
        for i in range(len(word)):
            if word[i] not in cur:
                return False
            cur = cur[word[i]]
        return None in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.data
        for i in range(len(prefix)):
            if prefix[i] not in cur:
                return False
            cur = cur[prefix[i]]
        return True
        