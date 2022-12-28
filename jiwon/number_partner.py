def get_dictionary(nums):
    dic = {}
    for num in nums:
        if dic.get(num):
            dic[num] += 1
        else:
            dic[num] = 1
    return dic


def solution(X, Y):
    answer = []
    dic_x = get_dictionary(X)
    dic_y = get_dictionary(Y)
    answer_set = set()
    for x in dic_x.keys():
        if dic_y.get(x) and dic_y[x] > 0:
            answer.extend(min(dic_y[x], dic_x[x]) * [x])
            answer_set.add(x)
    if not answer:
        return '-1'
    if len(answer_set) == 1 and list(answer_set)[0] == '0':
        return '0'
    answer = ''.join(sorted(answer, reverse=True))
    return answer