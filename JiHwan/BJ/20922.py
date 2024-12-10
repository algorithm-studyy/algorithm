# 같은 원소가 K개  이하 들어 있는 최장 연속 부분 수열의 길이를 구해라
if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    start, end = 0, 0
    count = [0] * (max(arr) + 1)
    answer = 0

    while end < N:
        if count[arr[end]] < K:
            count[arr[end]] += 1
            end += 1
        else:
            count[arr[start]] -= 1
            start += 1
        answer = max(answer, end - start)
    print(answer)