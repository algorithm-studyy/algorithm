import sys

n = int(sys.stdin.readline())
s = [[0] * 3 for i in range(n + 1)]

for i in range(3):
    s[1][i] = 1
for i in range(2, n + 1):
    s[i][0] = s[i - 1][1] + s[i - 1][2] % 9901  # 왼쪽에 호라이가 있을 때
    s[i][1] = s[i - 1][0] + s[i - 1][2] % 9901 # 오른쪽에 호랑이가 있을 때
    s[i][2] = s[i - 1][0] + s[i - 1][1] + s[i - 1][2] % 9901  # 호랑이가 한마리도 없을 때
print(sum(s[n]) % 9901)
