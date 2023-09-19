# 장르 별로 가장 많이 재생된 노래 두 개씩
# genres별로 dictionary 만들어서 재생
# 1. 장르별 노래로 정렬 desc
# 2. 장르 내 많이 재생된 노래 정렬 desc
# 3. 장르 내 재생 횟수가 같으면 고유번호로 정렬

# 장르에 속한 곡이 하나라면, 하나의 곡만 선택
def solution(genres, plays):
    answer = []
    dic = {genre: [] for genre in set(genres)}
    sum_dic = {genre: 0 for genre in set(genres)}
    for i, genre in enumerate(genres):
        dic[genre].append([plays[i], i])
        sum_dic[genre] += plays[i]
    for key, value in sorted(sum_dic.items(), key=lambda x: x[1], reverse=True):
        for cnt, item in enumerate(sorted(dic[key], key=lambda x: (-x[0], x[1]))):
            if cnt >= 2:
                break
            answer.append(item[1])
    return answer
