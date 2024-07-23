from sys import stdin


def solution():
    n, m = map(int, stdin.readline().split())
    word_count = dict()
    for _ in range(n):
        word = stdin.readline().strip()
        if len(word) >= m:
            word_count[word] = word_count.get(word, 0) + 1
    result = sorted(word_count.items(), key=lambda x: x[0])
    result.sort(key=lambda x: len(x[0]), reverse=True)
    result.sort(key=lambda x: x[1], reverse=True)
    print('\n'.join(key[0] for key in result))


solution()
