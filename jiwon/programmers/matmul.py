def solution(arr1, arr2):
    answer = []
    for y in range(len(arr1)):
        answer.append([])
        for x in range(len(arr2[0])):
            hap = 0
            for i in range(len(arr1[0])):
                hap += arr1[y][i] * arr2[i][x]
            answer[y].append(hap)
    return answer
