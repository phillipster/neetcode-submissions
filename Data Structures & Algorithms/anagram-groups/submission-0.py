class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        print(strs)
        for word in strs:
            chars = sorted(word)
            chars = tuple(chars)
            if chars not in map:
                map[chars] = [word]
            else:
                map[chars].append(word)
        return [map[key] for key in map]