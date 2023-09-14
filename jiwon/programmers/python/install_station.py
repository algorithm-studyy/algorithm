def solution(n, stations, w):
    answer = 0
    coverage = w * 2 + 1

    stations.append(n + w + 1)
    for i, station in enumerate(stations):
        distance = station - w - 1 if i == 0 else station - stations[i - 1] - coverage
        m, r = divmod(distance, coverage)
        answer += m if r == 0 else m + 1
    return answer
