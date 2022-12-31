def solution(X, Y):
    answer = ''
    dict_x = {str(n): 0 for n in range(10)}
    dict_y = {str(n): 0 for n in range(10)}
    
    for i in X:
        dict_x[i] +=1
    for j in Y:
        dict_y[j] +=1
        
    sorted_dict_x = sorted(dict_x.items(), key = lambda item: item[0], reverse = True)
    sorted_dict_y = sorted(dict_y.items(), key = lambda item: item[0], reverse = True)
    
    for key ,value in sorted_dict_x.item():
        if key
    
    
    return answer