from re import sub

def step_1(s):
    return ''.join([c for c in s if (c.isalpha() and c.islower()) or c == '-' or c == '_' or c == '.' or c.isdigit()])


def step_2(s):
    return sub(r'\.{2,}', '.', s)


def step_3(s):
    s = s[1:] if s[0] == '.' else s
    return s[:-1] if s and s[-1] == '.' else s


def step_4(s):
    return s if s else "a"


def step_5(s):
    s = s[:15]
    return s[:-1] if s and s[-1] == '.' else s


def step_6(s):
    while len(s) < 3:
        s += s[-1]
    return s


def solution(new_id):
    s = step_1(new_id.lower())
    s = step_2(s)
    s = step_3(s)
    s = step_4(s)
    s = step_5(s)
    return step_6(s)