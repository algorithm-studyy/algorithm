# 응시자이고, 아래와 오른쪽에 빈책상이 있다면, 대각선에 응시자가 있는지 확인


def iterate(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P':
                continue
            if (i < 4 and place[i + 1][j] == 'P') or (j < 4 and place[i][j + 1] == 'P'):
                return 0
            if i < 4 and j < 4 and (place[i][j + 1] == 'O' or place[i + 1][j] == 'O') and place[i + 1][j + 1] == 'P':
                return 0
            if j > 0 and i < 4 and (place[i][j - 1] == 'O' or place[i + 1][j] == 'O') and place[i + 1][j - 1] == 'P':
                return 0
            if i < 3 and place[i + 1][j] == 'O' and place[i + 2][j] == 'P':
                return 0
            if j < 3 and place[i][j + 1] == 'O' and place[i][j + 2] == 'P':
                return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(iterate(place))
    return answer
