from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    team = list(map(int, input().split()))
    count_team = Counter(team)
    new_team = [num for num in team if count_team[num] >= 6]
    scores = {}
    rank = 1
    for i in range(len(new_team)):
        if new_team[i] in scores:
            scores[new_team[i]].append(rank)
        else:
            scores[new_team[i]] = [rank]
        rank += 1

print(scores)



