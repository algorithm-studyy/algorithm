class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = []
        for word in s:
            answer.append(word)
            if len(answer) > 2:
                if answer == answer.reverse():



