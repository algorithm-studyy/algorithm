word = input()
window = word.count('a')
answer = []

for i in range(len(word)):
    b_count = 0
    for j in range(window):
        index = i + j
        if index > len(word) - 1:
            index -= len(word)
        if word[index] == 'b':
            b_count += 1
    answer.append(b_count)

print(min(answer))