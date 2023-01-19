def solution(today, terms, privacies):
    answer = []
    dict_term = {}
    year,month,day = today.split('.')
    
    for term in terms:
        alpha, number=term.split(' ')
        dict_term[alpha]=int(number)
               
    for i in range(len(privacies)):
        date, alpha = privacies[i].split(' ')
        date_year,date_month,date_day = date.split('.')
        date_month +=dict_term[alpha]
        
        if date_month >12:
            date_month = date_month -12
            date_year +=1
            
        if year < date_year:
            continue
        elif year == date_year:
            if month < date_month:
                continue
            elif month == date_month:
                if day < date_day-1:
                    continue
        
    
              
    return answer