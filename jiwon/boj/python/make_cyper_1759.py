from sys import stdin
from collections import Counter


def dfs(a, b):
    if b == l:
        print_str = ''.join(print_arr)
        counter = Counter(print_str)
        vowel = 0
        for letter in counter:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                vowel += counter[letter]
        if vowel >= 1 and len(print_str) - vowel >= 2:
            print(print_str)
        return
    for i in range(a, c):
        print_arr[b] = s[i]
        dfs(i + 1, b + 1)


if __name__ == '__main__':
    l, c = map(int, stdin.readline().split(" "))
    s = list(stdin.readline().strip().split(" "))
    s.sort()
    print_arr = ['0' for _ in range(l)]
    dfs(0, 0)

