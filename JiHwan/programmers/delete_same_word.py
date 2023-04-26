# 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾는다.
# 그 두개를 제거한다.
# 앞뒤로 문자열을 이어 붙인다.
# 문자열을 모두 제거한다면 종료

def solution(s):
    answer = 1
    arr = []
    for i in range(len(s)):
        if not arr:
            arr.append(s[i])
        else:
            if arr[-1] == s[i]:
                arr.pop()
            else:
                arr.append(s[i])
    if len(arr) != 0:
        answer = 0
    else:
        answer = 1

    return answer