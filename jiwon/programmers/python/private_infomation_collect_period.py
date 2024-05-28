def change_days(date):
    y, m, d = date.split('.')
    y_days = int(y[2:]) * 28 * 12
    m_days = int(m) * 28
    return y_days + m_days + int(d)


def get_end_days(sd, month):
    days = change_days(sd)
    return days + month


def get_terms_dict(terms):
    result = dict()
    for term in terms:
        k, v = term.split()
        result[k] = int(v) * 28
    return result


def solution(today, terms, privacies):
    answer = []
    td = get_terms_dict(terms)
    today_days = change_days(today)
    for i, private in enumerate(privacies, start=1):
        sd, term = private.split(" ")
        ed = get_end_days(sd, td[term])
        if today_days >= ed:
            answer.append(i)
    return answer
