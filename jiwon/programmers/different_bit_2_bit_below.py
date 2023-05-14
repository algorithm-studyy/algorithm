def make_binary(number):
    result = []
    a = -1
    while number > 0:
        if a == -1 and number % 2 == 0:
            a = len(result)
        result.append(str(number % 2))
        number //= 2
    if a == -1:
        result[-1] = '0'
        result.append('1')
    else:
        result[a] = '1'
        result[a - 1] = '0'
    return ''.join(result[::-1])


def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            b = make_binary(n)
            answer.append(int(b, 2))
    return answer
