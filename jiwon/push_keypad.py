def make_keypad():
    keypad = {0: [2, 4]}
    k = 1
    for i in range(1, 4):
        for j in range(1, 4):
            keypad[k] = [j, i]
            k += 1
    print(keypad)
    return keypad


def get_distance(location, keypad, num):
    return sum([abs(keypad[num][i] - location[i]) for i in range(2)])


def solution(numbers, hand):
    answer = ''
    left_location = [1, 4]
    right_location = [3, 4]
    keypad = make_keypad()

    for number in numbers:
        str_num = str(number)
        if str_num in '147':
            answer += 'L'
            left_location = keypad[number]
        elif str_num in '369':
            answer += 'R'
            right_location = keypad[number]
        else:
            rd = get_distance(right_location, keypad, number)
            ld = get_distance(left_location, keypad, number)
            if rd > ld:
                answer += 'L'
                left_location = keypad[number]
            elif rd < ld:
                answer += 'R'
                right_location = keypad[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_location = keypad[number]
                else:
                    answer += 'L'
                    left_location = keypad[number]
    return answer
