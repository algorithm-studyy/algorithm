from math import ceil


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = [c.lower() for c in s if c.isalnum()]
        len_s = len(alpha_s)
        for i in range(ceil(len_s // 2)):
            if alpha_s[i] != alpha_s[len_s - 1 - i]:
                return False
        return True
