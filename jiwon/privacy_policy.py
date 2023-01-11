def get_days(y, m, d, m2='0'):
    return int(y[2:]) * 28 * 12 + (int(m) + int(m2)) * 28 + int(d)


def solution(today, terms, privacies):
    answer = []
    today_days = get_days(*today.split('.'))
    terms_dic = dict(term.split(" ") for term in terms)

    for i, p in enumerate(privacies, start=1):
        date, term = p.split(' ')
        if today_days > get_days(*date.split('.'), terms_dic[term]) - 1:
            answer.append(i)
    return answer
