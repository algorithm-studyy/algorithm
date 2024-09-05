T = int(input())
for _ in range(T):

    n, k, t, m = map(int, input().split())

    dic = {i: {"score": [0] * (k + 1), "submit": 0, "time": 0} for i in range(1, n + 1)}
    print(dic)
    idx = 0
    for log_count in range(m):
        i, j, s = list(map(int, input().split()))

        dic[i]["score"][j] = max(dic[i]["score"][j], s)
        dic[i]["submit"] += 1
        dic[i]["time"] = idx
        idx += 1

    ord_dic = sorted(dic.items(), key=lambda item: (-sum(item[1]["score"]), item[1]["submit"], item[1]["time"]))

    for i in range(len(ord_dic)):
        if ord_dic[i][0] == t:
            print(i + 1)