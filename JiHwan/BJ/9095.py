num = int(input())
#count = 0
#root = []

def DP(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return DP(n-1)+DP(n-2)+DP(n-3)
        #for i in range():
            #for j in range(1,4):
                #root[i].append(j)
            
for i in range(num):
    n = int(input())
    print(DP(n))


