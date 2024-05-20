# n = 1 -> 1인 개수 / 1보다 큰 개수

def solution(N, stages):
    fail_ratio_dict = {i: 0 for i in range(1, N + 1)}
    for i in range(1, N + 1):
        not_clear = 0
        clear = 0
        for stage in stages:
            if i == stage:
                not_clear += 1
            if stage >= i:
                clear += 1
        fail_ratio_dict[i] = not_clear / clear if clear != 0 else 0
    return [k for k, v in sorted(fail_ratio_dict.items(), key=lambda x: x[1], reverse=True)]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
