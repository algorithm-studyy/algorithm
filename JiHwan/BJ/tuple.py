def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    for key in s:
        splited_key = key.split(',')
        print(splited_key)
        for argument in splited_key:
            if int(argument) not in answer:
                answer.append(int(argument))

    return answer