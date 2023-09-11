# 몫과 나머지 ..? 2일때는 그렇지만.
# n = 3 일때는 9-> 1 2 6, 5 2 2, 4 3 2
# n = 4, 9 -> 2 2 2 3, 3 1 3 2, 4 3 1 1
# n = 5, 9 -> 2 2 2 2 1
# 뭔가 s를 가장 n에 맞게끔 균일하게 나누는게 정답

def solution(n, s):
    if n > s:
        return [-1]
    answer = [s // n] * n
    for i in range(s % n):
        answer[i] += 1
    return sorted(answer)