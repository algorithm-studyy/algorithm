from sys import maxsize


def solution(gems):
    if len(gems) == 1:
        return [1, 1]
    answer = []
    all_gem_kind = len(set(gems))
    for s in range(len(gems) - all_gem_kind + 1):
        e = s
        unique_gems = set()
        while e < len(gems) and all_gem_kind != len(unique_gems):
            unique_gems.add(gems[e])
            e += 1
        if all_gem_kind == len(unique_gems):
            answer.append([s + 1, e])
    return sorted(answer, key=lambda x: ((x[1] - x[0]), x[0]))[0]
