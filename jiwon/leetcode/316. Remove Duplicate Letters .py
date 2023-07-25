from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = Counter(s), []
        for c in s:
            counter[c] -= 1
            if c in stack:
                continue
            while stack and c < stack[-1] and counter[stack[-1]] >= 1:
                stack.pop()
            stack.append(c)
        return ''.join(stack)