def solution(phone_book):
    phone_book.sort(key=len)
    dic = dict()
    for phone_number in phone_book:
        for i in range(len(phone_book[0]), len(phone_number)):
            dic[phone_number[:i]] = True
    for phone_number in phone_book:
        if phone_number in dic:
            return False
    return True
