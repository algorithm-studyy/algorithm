def solution(players, callings):
    position = {k: v for v, k in enumerate(players)}
    for c in callings:
        idx = position[c]
        prev_p = players[idx - 1]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        position[c], position[prev_p] = position[prev_p], position[c]
    return players
