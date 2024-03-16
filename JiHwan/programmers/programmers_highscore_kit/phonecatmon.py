def solution(nums):
    answer = 0

    nums_len = len(set(nums))
    result = int(len(nums) / 2)

    if nums_len > result:
        answer = result
    else:
        answer = nums_len
    return answer