from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])

    while q:
        word, cnt = q.popleft()
        count = 0
        if target not in words:
            answer = 0
            break
        elif word == target:
            answer = cnt
            break
        for i in range(len(words)):
            for j in range(len(word)):
                if word[j] != words[i][j]:
                    count += 1
            if count == 1:
                q.append([words[i], count + 1])

    return answer