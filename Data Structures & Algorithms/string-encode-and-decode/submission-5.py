class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        out = []
        for word in strs:
            out.append(str(len(word)))
            out.append('𓀴')
            out.append(word)
        return ''.join(out)


    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        out = []
        num = ''
        i = 0
        while i < len(s):
            if s[i] == '𓀴':
                out.append(s[i+1:i+int(num)+1])
                i += int(num)
                num = ''
            else:
                num += s[i]
            i += 1
        return out