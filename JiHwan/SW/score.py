from itertools import combinations

T = int(input())
answer = set()
for t in range(1, T + 1):
    n = int(input())
    score = list(map(int, input().split()))
    for i in range(1, n + 1):
        comb = list(combinations(score, i))
        for c in comb:
            answer.add(sum(c))
    print("#{} {}".format(t, len(answer)+1))
