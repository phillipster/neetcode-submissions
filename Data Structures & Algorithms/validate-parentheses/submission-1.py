class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 == 1:
            return False
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] in '[{(':
                stack.append(s[i])
            else:
                if not stack: return False
                prev = stack.pop()
                if s[i] == ')' and prev != '(':
                    return False
                if s[i] == ']' and prev != '[':
                    return False
                if s[i] == '}' and prev != '{':
                    return False
        if stack:
            return False
        return True
