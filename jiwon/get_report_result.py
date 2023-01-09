def solution(id_list, report, k):
    answer = [0 for i in id_list]
    reporters = {key: i for i, key in enumerate(id_list)}
    reported_cnt = dict()
    reported_list = dict()
    for r in set(report):
        reporter, reported = r.split(" ")
        if reported in reported_list:
            reported_cnt[reported] += 1
            reported_list[reported].add(reporter)
        else:
            reported_list[reported] = {reporter}
            reported_cnt[reported] = 1

    for key, value in reported_list.items():
        if reported_cnt[key] < k:
            continue
        for v in value:
            answer[reporters[v]] += 1
    return answer
