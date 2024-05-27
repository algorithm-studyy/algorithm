def get_location():
    result = dict()
    for i in range(3):
        for j in range(3):
            result[i * 3 + j + 1] = [i, j]
    result[0] = [3, 1]
    return result


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solution(numbers, hand):
    answer = ''드
    left = [3, 0]
    right = [3, 2]
    phone_loc = get_location()

    for number in numbers:
        if number == 0 or number % 3 == 2:
            left_distance = get_distance(left, phone_loc[number])
            right_distance = get_distance(right, phone_loc[number])
            if left_distance < right_distance:
                left = phone_loc[number]
                answer += "L"
            elif left_distance > right_distance:
                right = phone_loc[number]
                answer += "R"
            else:
                if hand == "left":
                    left = phone_loc[number]
                    answer += "L"
                else:
                    right = phone_loc[number]
                    answer += "R"
        elif number % 3 == 1:
            answer += "L"
            left = phone_loc[number]
        elif number % 3 == 0:
            answer += "R"
            right = phone_loc[number]

    return answer
