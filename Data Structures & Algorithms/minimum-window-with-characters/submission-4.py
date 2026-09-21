from math import inf
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = r = left_res = right_res = 0
        min_len = inf
        t_hash = defaultdict(int)
        for c in t:
            t_hash[c] += 1
        s_hash = defaultdict(int)
        have, need = 0, len(t_hash)

        while l <= r < len(s):
            s_hash[s[r]] += 1
            if s[r] in t_hash and s_hash[s[r]] == t_hash[s[r]]:
                have += 1

            while have == need:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    left_res, right_res = l, r
                if s[l] in t_hash and s_hash[s[l]] == t_hash[s[l]]:
                    have -= 1
                s_hash[s[l]] -= 1
                l += 1
            
            r += 1
        return s[left_res:right_res+1] if min_len < inf else ''
