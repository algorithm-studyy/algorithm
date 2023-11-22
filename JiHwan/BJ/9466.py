def dfs(x):
    global count

    visited[x] = 1
    term.append(x)
    if visited[arr[x] - 1] == 1:
        if arr[x] - 1 in term:
            term_index = term.index(arr[x] - 1)
            if term_index >= 0:
                count_index = term[term_index:]
                count -= len(count_index)
            return
    else:
        dfs(arr[x] - 1)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        visited = [0] * n
        count = n

        for i, k in enumerate(arr):
            if visited[i] == 0:
                term = []
                dfs(i)
        print(count)
