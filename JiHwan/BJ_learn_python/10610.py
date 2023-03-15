N = list(map(int, input()))
total = 0
N.sort(reverse=True)

if N[len(N)-1] == 0:
    for i in range(len(N)):
        total += N[i]
    if total % 3 == 0:
        print(''.join(map(str, N)))
    else:
        print(-1)
else:
    print(-1)