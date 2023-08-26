def solution(n):
    answer = 0
    num = bin(n)
    num_count = num.count('1')
    for i in range(n+1, 1000000):
        big_num = bin(i)
        big_count = big_num.count('1')
        if num_count == big_count:
            answer = i
            break
    return answer