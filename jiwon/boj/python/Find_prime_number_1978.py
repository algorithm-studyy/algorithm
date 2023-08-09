from sys import stdin


def get_line_input():
    stdin.readline()
    solution()


def solution():
    nums = list(map(int, stdin.readline().split(" ")))
    n = max(nums)
    answer = 0
    spf = [0 for _ in range(n + 1)]
    prime_num = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            prime_num.append(i)
            spf[i] = i
            if i in nums:
                answer += 1
        for j in range(n):
            if i * prime_num[j] > n:
                break
            spf[i * prime_num[j]] = prime_num[j]
            if i % prime_num[j] == 0:
                break
    print(answer)


get_line_input()
