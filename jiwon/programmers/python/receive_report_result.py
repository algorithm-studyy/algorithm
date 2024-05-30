def solution(id_list, report, k):
    answer = [0] * len(id_list)
    rd = {k: set() for k in id_list}
    rd2 = {k: set() for k in id_list}
    rk = {k: idx for idx, k in enumerate(id_list)}
    stop = set()
    for r in report:
        a, b = r.split()
        rd[a].add(b)
        rd2[b].add(a)
        if len(rd2[b]) >= k:
            stop.add(b)

    for k, v in rd.items():
        answer[rk[k]] = len(v & stop)
    return answer
