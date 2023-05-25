# 최소의 수를 그 때마다 고르면 되지 않을까 ?
# 정렬해서 A[0] * B[-1] or A[-1] or B[0]

def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
