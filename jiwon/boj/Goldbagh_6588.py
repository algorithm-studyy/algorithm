from sys import stdin


def get_line_input():
    n_list = []
    while True:
        n = int(stdin.readline())
        n_list.append(n)
        if n == 0:
            break
    solution(n_list[:-1])


def solution(n):
    prime_nums = get_odd_prime_number(n)
    prime_dict = {key: True for key in prime_nums}
    for i in n:
        for prime in prime_nums:
            if i - prime in prime_dict:
                print(f'{i} = {prime} + {i - prime}')
                break


def get_odd_prime_number(a):
    spf = [0 for _ in range(a + 1)]
    prime_nums = []
    for i in range(2, a + 1):
        if spf[i] == 0:
            spf[i] = i
            prime_nums.append(i)
        for j in range(a + 1):
            if i * prime_nums[j] > a:
                break
            spf[i * prime_nums[j]] = prime_nums[j]
            if i % prime_nums[j] == 0:
                break

    return list(filter(lambda x: x % 2 == 1, prime_nums))


get_line_input()
