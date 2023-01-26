import sys
from collections import deque

sentence = sys.stdin.readline().rstrip()
sentence_1 = deque([])
temp = []
answer = []

for i in range(len(sentence)):
    sentence_1.append(sentence[i])
    if sentence_1[i]=='>':
        for j in range(len(sentence_1)):
            answer.append(sentence_1.popleft())
    elif sentence_1[i] == '<' and len(sentence_1)!=1:
        sentence_1 = sentence_1[::-1]
        temp.append(sentence_1.pop(len(sentence_1)-1))
    elif sentence_1[i]== ' ':
        sentence_1 = sentence_1[::-1]