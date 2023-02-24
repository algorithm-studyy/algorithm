n = int(input())
sign = list(input().split())
visited = [False] * 10
min_ans,max_ans="",""


def compare(i,j,k):
    if k == '>':
        return i>j
    else:
        return i<j
    return True


def DFS(cnt,s):
    global max_ans, min_ans
    if cnt > n:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or compare(cnt,str(i),""):
                visited[i] = True
                DFS(cnt+1,s+str(i))
                visited[i] = False

DFS(0, "")
print(max_ans)
print(min_ans)