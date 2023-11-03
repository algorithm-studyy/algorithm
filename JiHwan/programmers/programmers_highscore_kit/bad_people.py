from itertools import permutations


def check_id(user, bann):
    for i in range(len(user)):
        if len(bann[i]) != len(user[i]):
            return False
        for j in range(len(user[i])):
            if user[i][j] != bann[i][j] and bann[i][j] != '*':
                return False
    return True


def solution(user_id, banned_id):
    arr = []
    pair_user = list(permutations(user_id, len(banned_id)))

    for user in pair_user:
        if check_id(user, banned_id):
            user = set(user)
            if user not in arr:
                arr.append(user)

    answer = len(arr)
    return answer
