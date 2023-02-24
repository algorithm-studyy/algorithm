def solution(s):
    answer = 0
    first_word = 0
    second_word = 0
    
    for i in s:
        if first_word == second_word :
            answer +=1
            k=i
        if k==i:
            first_word +=1
        else :
            second_word +=1
            
        
        
    return answer