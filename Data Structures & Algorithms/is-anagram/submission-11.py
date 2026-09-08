class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}
        for c in s:
            if c not in s_map:
                s_map[c] = 1
            else:
                s_map[c] += 1
        for c in t:
            if c not in t_map:
                t_map[c] = 1
            else:
                t_map[c] += 1
        for key in s_map:
            if key not in t_map or s_map[key] != t_map[key] or len(s_map) != len(t_map):
                return False
        return True