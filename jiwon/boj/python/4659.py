
def check1(s):
    return any(c in 'aeiou' for c in s)


def check2(s):
    prev_mo = 0
    prev_ja = 0
    mo = 'aeiou'
    for c in s:
        if c in mo:
            prev_ja = 0
            prev_mo += 1
            if prev_mo == 3:
                return False
        else:
            prev_mo = 0
            prev_ja += 1
            if prev_ja == 3:
                return False
    return True


def check3(s):
    prev_char = ''
    for c in s:
        if prev_char not in 'eo' and prev_char == c:
            return False
        prev_char = c
    return True


def solution():
    while True:
        s = input()
        if s == 'end':
            break
        if check1(s) and check2(s) and check3(s):
            print(f'<{s}> is acceptable.')
        else:
            print(f'<{s}> is not acceptable.')


solution()
