# 1. 대문자로 이뤄진 딕셔너리 만들기
# 2. 다음 글자 없다면 다음 글자와 현재 입력을 딕셔너리에 추가하고 출력
# !! 그러면 사전에 검색할 때는 몇글자까지 검색해봐야할까 ?
# - 사전에 추가할 때 길이를 저장 min(최대길이, 남은 문자열 수)

from string import ascii_uppercase


def solution(msg):
    answer = []
    dic = {k: i + 1 for i, k in enumerate(ascii_uppercase)}
    max_len = 1
    i = 0
    while i < len(msg):
        for s in range(min(max_len, len(msg) - i), 0, -1):
            next_i = i + s
            w = msg[i:next_i]
            if w not in dic:
                continue
            answer.append(dic[w])
            i += s

            if next_i >= len(msg):
                continue
            wc = w + msg[next_i]
            if wc not in dic:
                dic[wc], max_len = len(dic) + 1, max(max_len, len(wc))
            break
    return answer
