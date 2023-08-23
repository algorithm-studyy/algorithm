def permutation(num, i):
    global answer = []
    if num >= i:
        answer.append(arr[:])
        return
    else:
        for i in range(i):


def solution(n, k):
    global answer = []
    arr = [i + 1 for i in range(n)]
    level = len(arr)
    permutation(level, n)
    return answer