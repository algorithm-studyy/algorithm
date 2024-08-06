T = int(input())
#팀의 수, 문제 수, 내 팀ID, 로그 엔트리개수

for _ in range(T):
    n, k, t, m = map(int, input().split())
    arr = [[0 for _ in range(n + 1)] for _ in range(k + 2)]
    for _ in range(m):
        i, j, s = map(int, input().split())
        if arr[j][i] <= s:
            arr[j][i] = s
            arr[k + 1][i] += 1
        else:
            arr[k + 1][i] += 1
        print(arr)
