def solution(ingredient):
    answer = 0
    n = len(ingredient)
    
    for i in range(n):
        if ingredient[i:i+4] == [1,2,3,1]:
            del ingredient[i:i+4]
            i = i-1
            answer +=1
    return answer