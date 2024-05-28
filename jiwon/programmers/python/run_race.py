def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]


def solution(players, callings):
    pd = {player: rank for rank, player in enumerate(players)}
    for c in callings:
        idx = pd[c]
        swap(pd, c, players[idx - 1])
        swap(players, idx, idx - 1)
    return players
