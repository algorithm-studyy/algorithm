def solution(n, words):
    answer = [0, 0]
    used_word = []
    used_word.append(words[0])
    count = 0

    for i in range(1, len(words)):
        count += 1
        if words[i] not in used_word and list(words[i - 1])[-1] == list(words[i])[0]:
            used_word.append(words[i])
        else:
            answer[0] = count % n + 1
            answer[1] = count // n + 1
            break

    return answer