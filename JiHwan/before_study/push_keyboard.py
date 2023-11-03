def solution(numbers, hand):
    answer = ''
    
    now_left_position = 10
    
    now_right_position = 12
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            now_left_position = i
        elif i in [3,6,9]:
            answer += 'R'
            now_right_position = i
        else:
            if (abs(now_right_position - i)) < (abs(now_left_position -i)):
                answer +='R'
                now_right_position = i
            elif (abs(now_left_position - i))<(abs(now_right_position - i)):
                answer +='L'
                now_left_position = i
            elif (abs(now_left_position - i))==(abs(now_right_position - i)):
                if (hand == 'left'):
                    answer +='L'
                    now_left_position = i
                elif hand == 'right':
                    answer +='R'
                    now_right_position = i
                
        

            
            
            
    return answer