from heapq import heappush, heappop


def solution(operations):
    minh, maxh = [], []
    insert_list, min_list, max_list = [], [], []
    for operation in operations:
        o, v = operation.split()
        if o == 'I':
            v = int(v)
            insert_list.append(v)
            heappush(minh, v)
            heappush(maxh, (-v, v))
        elif o == 'D' and v == '-1':
            if minh:
                min_list.append(heappop(minh))
        else:
            if maxh:
                max_list.append(heappop(maxh))
        if len(insert_list) <= len(min_list) + len(max_list):
            minh, maxh = [], []

    insert_len, min_len, max_len = len(insert_list), len(min_list), len(max_list)
    if insert_len <= min_len + max_len:
        return [0, 0]
    if insert_len + 1 == min_len + max_len:
        value = [v for v in insert_list if not v in min_list and not v in max_list]
        return [value, value]
    return [maxh[0][1], minh[0]]