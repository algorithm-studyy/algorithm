class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = re.sub(r"[^a-zA-Z0-9\s]", ' ', paragraph).lower().split(' ')
        word_count = Counter(word)
        word_count[''] = 0
        print(word_count)
        for banned_word in banned:
            word_count[banned_word] = 0

        return word_count.most_common(1)[0][0]

