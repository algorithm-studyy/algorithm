n = int(input())
first_word = list(input())
answer = 0

for _ in range(n - 1):
    compare = first_word[:]
    word = input()
    count = 0
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            count += 1
    if count < 2 and len(compare) < 2:
        answer += 1
print(answer)
