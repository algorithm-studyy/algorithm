def find_fail_team(records):
    team_count = dict()
    result = set()
    for record in records:
        team_count[record] = team_count.get(record, 0) + 1
    for key, value in team_count.items():
        if value < 6:
            result.add(key)

    return result


def calculate_team_score(lst):
    return sum(lst[:4]), scores[4]


def solution():
    for _ in range(int(input())):
        _ = int(input())
        records = list(map(int, input().split()))
        fail_team = find_fail_team(records)
        rank = 1
        team_sum = {k: list() for k in set(records) if k not in fail_team}
        for record in records:
            if record in fail_team:
                continue
            team_sum[record].append(rank)
            rank += 1
        # dict_items([(1, [1, 4, 6, 7, 9, 12])
        result = sorted(team_sum.items(), key=lambda x: calculate_team_score(x[1]))
        print(result[0][0])


solution()
