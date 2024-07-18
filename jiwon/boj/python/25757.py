from sys import stdin


n, t = stdin.readline().strip().split()
play = {k: v + 1 for v, k in enumerate(['Y', 'F', 'O'])}
player = set()
for _ in range(int(n)):
    player.add(stdin.readline().strip())


print(len(player) // play[t])
