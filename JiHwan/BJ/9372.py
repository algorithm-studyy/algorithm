from collections import defaultdict


if __name__ == "__main__":

    t = int(input())

    for i in range(t):
        n, m = map(int, input().split())
        plane = defaultdict(list)
        cnt = 0
        for _ in range(m):
            a, b = map(int, input().split())
            plane[a].append(b)
            plane[b].append(a)
        visited = defaultdict(bool)
        visited_land = [1]

        while visited_land:
            land = visited_land.pop()
            visited[land] = True
            next_land = plane[land]

            for country in next_land:
                if not visited[country] and country not in visited_land:
                    visited_land.append(country)
                    cnt += 1

        print(cnt)