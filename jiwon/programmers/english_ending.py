def solution(n, words):
    answer = [0, 0]
    use_words = set()
    for i, word in enumerate(words):
        if i == len(words) - 1:
            continue
        if word[-1] != words[i + 1][0] or words[i + 1] in use_words:
            answer[0] = (i + 1) % n + 1
            answer[1] = (i + 1) // n + 1
            break
        use_words.add(word)
    return answer
