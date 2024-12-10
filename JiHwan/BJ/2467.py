if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    print(graph)