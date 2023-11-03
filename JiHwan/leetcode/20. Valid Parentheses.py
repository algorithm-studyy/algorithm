class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        gwalho = {'{': '}', '(': ')', '[': ']'}
        for i in s:
            if i in gwalho:
                stack.append(i)
            else:
                if not stack or gwalho[stack.pop()] != i:
                    return False

        if stack:
            return False
        else:
            return True

