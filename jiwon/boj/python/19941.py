from collections import deque


def solution():
    n, k = map(int, input().split())
    hps = list(input().strip())
    result = 0

    for i, hp in enumerate(hps):
        if hp != 'P':
            continue
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and hps[j] == 'H':
                hps[j] = 'C'
                result += 1
                break
    print(result)


solution()
