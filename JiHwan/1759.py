import sys

def DFS(depth,start):
    vo = 0
    co = 0
    if depth == n :
        for  i in range(n):
            if vowel[i] in answer:
                vo +=1
            else:
                co +=1
        
            if vo >=1 and co >= 2:
                print(''.join(answer))

    for i in range(0,c):
        answer.append(word[i])
        DFS(depth+1,start+1)
        answer.pop()


    



n ,c = map(int, sys.stdin.readline().split())
word = (list(sys.stdin.readline().split()))
word.sort()
vowel = ['a','e','i','o','u']
answer = []

DFS(0,0)

