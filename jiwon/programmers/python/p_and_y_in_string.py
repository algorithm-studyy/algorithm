def solution(s):
    s = s.lower()
    return len([c for c in s if c == 'y']) == len([c for c in s if c == 'p'])


print(solution("pPoooyY"))
print(solution("Pyy"))
