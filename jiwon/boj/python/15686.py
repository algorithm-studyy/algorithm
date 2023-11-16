# N x N 도시 -> 빈칸, 치킨집, 집
# 도시는 (r, c)
# 도시 치킨 거리 = sum(치킨 거리)
# 폐업시키지 않을 치킨집 M개일 때, 도시의 치킨 거리 최솟값.

### 풀이
# 1. 치킨 집, 집 위치 찾기
# 2. M 개 뽑기 -> 최솟 값 찾기
from itertools import combinations
from sys import stdin, maxsize


def get_house():
    result = []
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 1:
                result.append((i, j))
    return result


def get_chicken():
    result = []
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 2:
                result.append((i, j))
    return result


def get_distance(house, chicken):
    result = 0
    for h in house:
        num = maxsize
        for c in chicken:
            num = min(num, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        result += num
    return result


def solution():
    result = maxsize
    house, chicken = get_house(), get_chicken()
    for choice_chicken in combinations(chicken, m):
        result = min(result, get_distance(house, choice_chicken))
    print(result)


if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    board = [list(map(int, stdin.readline().split())) for _ in range(n)]
    solution()
