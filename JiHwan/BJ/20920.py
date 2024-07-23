from collections import Counter
import sys

n, m = map(int, input().split())
word_list = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    if len(word) < m:
        continue
    else:
        word_list.append(word)

count_word = Counter(word_list)
sorted_word = sorted(count_word.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

sorted_word_list = [word[0] for word in sorted_word]
print('\n' .join(sorted_word_list))
