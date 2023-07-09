# Time: 29.14 / Memory : 59.73
from re import sub
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = sub(r'[^a-z ]', ' ', paragraph.lower()).split(" ")
        banned = {k: True for k in banned}
        print(paragraph)
        for k, v in Counter(paragraph).most_common():
            if not k or k in banned:
                continue
            return k
        return -1
