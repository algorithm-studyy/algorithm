def room(place):
    people = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append([i, j])

    for i in range(len(people)):
        r1, c1 = people[i]
        for j in range(i + 1, len(people)):
            r2, c2 = people[j]
            distance = abs(r2 - r1) + abs(c2 - c1)

            if distance == 1:
                return 0

            if distance == 2:
                if r1 == r2:
                    if place[r1][c1 + 1] == 'O':
                        return 0
                if c1 == c2:
                    if place[r1 + 1][c1] == 'O':
                        return 0
                else:


def solution(places):
    answer = []
    for place in places:
        answer.append(room(place))
    return answer