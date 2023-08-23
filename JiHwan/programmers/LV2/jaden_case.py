def solution(s):
    answer = " "
    arr = list(s)

    for i in range(1, len(arr)):
        if arr[i - 1] == ' ':
            arr[i] = arr[i].upper()
        elif arr[i - 1] != ' ':
            arr[i] = arr[i].lower()
    arr[0] = arr[0].upper()
    arr = ''.join(arr)

    return arr
