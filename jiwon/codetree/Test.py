from itertools import groupby
from operator import itemgetter

data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Alice', 'age': 22}]
data.sort(key=itemgetter('name'))  # 키 기준 정렬

grouped_data = groupby(data, key=itemgetter('name'))

for key, group in grouped_data:
    print(key, list(group))
