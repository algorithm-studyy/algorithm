N = int(input())
M = int(input())
locate = list(map(int, input().split()))

if M == 1:
    height = max(locate[0], N - locate[0])
else:
    height = locate[0]
    for i in range(1, len(locate)):
        if (locate[i] - locate[i - 1]) % 2 == 0:
            height = max(height, ((locate[i] - locate[i - 1]) // 2))
        else:
            height = max(height, ((locate[i] - locate[i - 1]) // 2) + 1)
    height = max(height, N - locate[-1])
print(height)
