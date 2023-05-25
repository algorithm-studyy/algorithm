def solution(want, number, discount):
    answer = 0
    dic = {w: n for w, n in zip(want, number)}
    hap = sum(number)
    for i in range(len(discount) - hap + 1):
        discount_dic = dict()
        for j in range(i, hap + i):
            if discount[j] not in discount_dic:
                discount_dic[discount[j]] = 1
            else:
                discount_dic[discount[j]] += 1
        if dic == discount_dic:
            answer += 1
    return answer
