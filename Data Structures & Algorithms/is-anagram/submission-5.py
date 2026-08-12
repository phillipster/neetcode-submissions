class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for char in s:
            if char not in dict_s:
                dict_s[char] = 1
            else:
                dict_s[char] += 1
        dict_t = {}
        for char in t:
            if char not in dict_t:
                dict_t[char] = 1
            else:
                dict_t[char] += 1
        for char in dict_s:
            if char not in dict_t or dict_s[char] != dict_t[char]:
                return False
        for char in dict_t:
            if char not in dict_s:
                return False
        return True