from sys import maxsize


def solution(gems):
    answer = [0, maxsize]
    all_gem_kind = len(set(gems))
    s, e = 0, -1
    gems_cnt = dict()
    while e < len(gems):
        if len(gems_cnt) == all_gem_kind:
            if e - s < answer[1] - answer[0]:
                answer = [s, e]
            else:
                gems_cnt[gems[s]] -= 1
                if gems_cnt[gems[s]] == 0:
                    del gems_cnt[gems[s]]
                s += 1
        else:
            e += 1
            if e == len(gems):
                break
            gems_cnt[gems[e]] = gems_cnt.get(gems[e], 0) + 1

    return [answer[0] + 1, answer[1] + 1]
