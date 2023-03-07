N, K = map(int, input().split())
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in range(N-1, -1, -1):
    count += K//coin_lst[i]
    K = K % coin_lst[i]
print(count)