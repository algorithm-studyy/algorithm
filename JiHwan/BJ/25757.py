import sys

n, k = sys.stdin.readline().split()

people = set()

for _ in range(int(n)):
    name = sys.stdin.readline().rstrip()
    people.add(name)

if k == 'Y':
    print(len(people))
elif k == 'F':
    print(len(people) // 2)
else:
    print(len(people) // 3)