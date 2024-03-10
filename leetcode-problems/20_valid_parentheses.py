class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openner = ["(", "[", "{"]
        closer = [")", "]", "}"]
        for c in s:
            if c in openner: 
                stack.append(c)
            else:
                if not stack: return False
                if closer[openner.index(stack[-1])] == c:
                    stack.pop(-1)
                else:
                    return False
        if stack: return False
        return True