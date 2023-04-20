def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    hap = 0
    while hap < k:
        hap += sorted_dic[answer][1]
        answer += 1
    return answer
