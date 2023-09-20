def solution(genres, plays):
    answer = []

    playlist = {}
    toplist = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in playlist:
            playlist[g] = [(i, p)]
        else:
            playlist[g].append((i, p))

        if g not in toplist:
            toplist[g] = p
        else:
            toplist[g] += p

    while len(toplist) != 0:
        top_genre = max(toplist, key=toplist.get)
        del toplist[top_genre]

        top_playlist = sorted(playlist[top_genre], key=lambda x: x[1], reverse=True)

        for i in range(len(top_playlist)):
            if i >= 2:
                break
            else:
                answer.append(top_playlist[i][0])

    return answer