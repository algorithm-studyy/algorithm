def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]
    new_lotto = [item for item in lottos if item != 0]
    zero_count = len(lottos) - len(new_lotto)
    hit_count = 0
    for lotto in new_lotto:
        if lotto in win_nums:
            hit_count += 1

    return [answer[hit_count + zero_count], answer[hit_count]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))

