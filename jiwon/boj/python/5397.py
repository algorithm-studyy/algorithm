from sys import stdin


#ABC<<DE -> left [A, B, C] -> left [A], right [C, B] -> [A D E], [C, B]
def process_list(lst):
    left = [] # 커서 기준 왼
    right = [] # 커서 기준 오
    for i in lst:
        if left and i == '<':
            right.append(left.pop())
        if right and i == '>':
            left.append(right.pop())
        if left and i == '-':
            left.pop()
        if i.isalnum():
            left.append(i)
    while right:
        left.append(right.pop())
    return left


for _ in range(int(stdin.readline())):
    t = list(stdin.readline().strip())
    print(''.join(process_list(t)))
