from sys import stdin
from collections import Counter


def solution():
    n = int(stdin.readline())
    words = [stdin.readline().strip() for _ in range(n)]
    result = 0
    word = words[0]
    for j in range(1, n):
        word2 = words[j]
        if abs(len(word) - len(word2)) > 1:
            continue
        word_counter = Counter(word)
        word2_counter = Counter(word2)
        word_counter.subtract(word2_counter)
        diff = sum(word_counter.values())
        diff_abs = sum(map(abs, word_counter.values()))
        if diff <= 1 and diff_abs <= 2:
            result += 1
    print(result)


solution()
