class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            counts = [0]*26
            for char in s:
                counts[ord(char)-ord('a')] += 1
            m[tuple(counts)].append(s)
        return list(m.values())