import re
from functools import cmp_to_key


def compare(a, b):
    v1_list = [a[0].upper(), int(a[1].replace('^[0]+', ''))]
    v2_list = [b[0].upper(), int(b[1].replace('^[0]+', ''))]
    for v1, v2 in zip(v1_list, v2_list):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
    return 0


# 처음에 등장하는 숫자만 파악해서 분리
# 정렬 키 바꿔서 사용
def solution(files):
    answer = []
    file_list = []
    # 처음에 등장하는 숫자로 분리
    for file in files:
        match_string = re.search('[0-9]+', file)
        head = file[:match_string.start()]
        number = file[match_string.start():match_string.end()]
        tail = file[match_string.end():]
        file_list.append((head, number, tail))
    file_list.sort(key=cmp_to_key(compare))

    for head, number, tail in file_list:
        answer.append(head + number + tail)
    return answer


#######################
# 더 좋은 답
# import re

# def solution(files):

#     def key_function(fn):
#         head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
#         return [head,int(number)]

#     return sorted(files, key = lambda x: key_function(x.lower()))
