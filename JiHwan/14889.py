import sys

power1 = 0
power2 = 0
def DFS(depth,key):
    global gap
    for i in range(0,n):
        if i not in start:
            link.append(i)
            power1 = arr[start[i]][i]+arr[i][start[i]]
            power2 = arr[link[i]][i]+arr[i][link[i]]
            gap = power1-power2
            answer.append(gap)
    
            

    for i in range(n):
        start.append(i)
        DFS(depth+1,key+1)
        start.pop()

n = int(input())
start = []
link = []
answer = []
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
DFS(0,0)
answer.sort()
print(answer[0])