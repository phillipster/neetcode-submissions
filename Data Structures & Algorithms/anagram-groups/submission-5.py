class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            curr = tuple(sorted(Counter(s).items()))
            m[curr].append(s)
        return list(m.values())