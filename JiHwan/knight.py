def num_division(num,limit,power):
    divide = 0
    for i in range(1, int(num**(1/2))+1):
        if num%i == 0:
            divide +=1
            if num%i != i :
                divide +=1
    if divide >limit:
        return power
    
    return divide

def solution(number, limit, power):
    answer = 1
    for i in range(1 , number+1):
        total_divide = num_division(i,limit,power)
        answer +=total_divide
        
    
    return answer