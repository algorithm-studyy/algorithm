from collections import defaultdict


def length(word):
    min_i = 100001
    max_i = 0
    for idx_list in word.values():
        if len(idx_list) < K:
            continue
        for i in range(len(idx_list) - K + 1):
            min_i = min(min_i, idx_list[i + K - 1] - idx_list[i])
            max_i = max(max_i, idx_list[i + K - 1] - idx_list[i])
    return min_i + 1, max_i + 1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        W = input().strip()
        K = int(input())
        dic = defaultdict(list)
        for i, k in enumerate(W):
            if W.count(k) >= K:
                dic[k].append(i)
        if not dic:
            print(-1)
        else:
            print(*length(dic))
