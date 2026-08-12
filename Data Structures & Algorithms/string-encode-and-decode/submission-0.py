class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_lst = []
        for word in strs:
            enc_lst.append(str(len(word)) + '#' + word)
        return ''.join(enc_lst)

    def decode(self, s: str) -> List[str]:
        out_lst = []
        i = 0
        num = ''
        while i < len(s):
            if s[i] != '#':
                num += s[i]
                i += 1
            else:
                out_lst.append(s[i+1:i+int(num)+1])
                i += int(num) + 1
                num = ''
        return out_lst
                    
                
                    
                