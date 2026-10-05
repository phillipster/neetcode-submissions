class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        sm = min(strs, key=len)
        out = ''
        if len(sm) == 0:
            return ''
        for i in range(len(sm)):
            curr_char = sm[i]
            for s in strs:
                if s[i] != curr_char:
                    return out
            out += curr_char
        return out