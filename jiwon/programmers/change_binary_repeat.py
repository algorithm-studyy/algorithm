def solution(s):
    cnt = 0
    i = 0
    while True:
        if s == '1':
            break
        c = [ch for ch in s if ch == '1']
        diff = len(s) - len(c)
        cnt += diff
        i += 1
        s = format(len(c), 'b')
    return [i, cnt]
