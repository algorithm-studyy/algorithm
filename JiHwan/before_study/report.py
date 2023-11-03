def solution(id_list, report, k):
    answer = []
    dic_report = {id: [] for id in id_list}
    
    for i in set(report):
        report = i.split(' ')
        print(report)
        dic_report[report[0]].append(report[1])
        
    print(dic_report)
    #for key, value in dic_report.items():
        
    return answer