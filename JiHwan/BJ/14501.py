import sys

N = int(input())
day = dict()
answer = []
sum = 0

def DFS(depth,sum):
    if depth == N:
        for i in answer:
            answer.sort(reverse=True)
            print(answer[0])
        
    if depth < N :
        sum += int(day[T])
        DFS(depth+T,sum)


for i in range(N):
    T, P = (list(sys.stdin.readline().split()))
    day[T]=P
    DFS(0,0)
