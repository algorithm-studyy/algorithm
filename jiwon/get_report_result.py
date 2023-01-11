def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    reported_list = dict()
    for r in set(report):
        reporter, reported = r.split(" ")
        if reported in reported_list:
            reported_list[reported].add(reporter)
        else:
            reported_list[reported] = {reporter}

    for key, value in reported_list.items():
        if len(reported_list[key]) < k:
            continue
        for v in value:
            answer[id_list.index(v)] += 1
    return answer
