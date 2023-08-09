from sys import stdin


def get_two_input():
    a, b = map(int, stdin.readline().strip().split(" "))
    nums = list(map(int, stdin.readline().strip().split(" ")))
    solution(nums, b, a)


def solution(nums, s, length):
    answer = 0
    limit = 1 << length
    for i in range(1, limit):
        hap = 0
        for j in range(length):
            if i & (1 << j):
                hap += nums[j]
        if hap == s:
            answer += 1
    print(answer)


get_two_input()
