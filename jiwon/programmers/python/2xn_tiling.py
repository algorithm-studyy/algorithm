def solution(n):
    a, b = 1, 2

    for i in range(2, n):
        a, b = b, (a + b) % 1_000_000_007
    return b
