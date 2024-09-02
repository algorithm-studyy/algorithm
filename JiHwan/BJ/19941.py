# n, k = map(int, input().split())
# arr = list(input())
# count = 0
# for i in range(n):
#     if arr[i] == 'P':
#         for j in range(i-k, i+k+1):
#             if 0 <= j < n and arr[j] == 'H':
#                 count += 1
#                 arr[j] = 'D'
#                 break
#
# print(count)


N, K = map(int, input().split())
ham = list(input())
count = 0
for i in range(len(ham)):
    if ham[i] == 'P':
        for j in range(i - K, i + K + 1):
            if 0 <= j < N and ham[j] == 'H':
                count += 1
                ham[j] = 'D'
                break
print(count)


