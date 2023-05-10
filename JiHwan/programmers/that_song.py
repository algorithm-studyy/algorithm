def change(melody):
    if 'A#' in melody:
        melody = melody.replace('A#', 'a')
    if 'C#' in melody:
        melody = melody.replace('C#', 'c')
    if 'D#' in melody:
        melody = melody.replace('D#', 'd')
    if 'F#' in melody:
        melody = melody.replace('F#', 'f')
    if 'G#' in melody:
        melody = melody.replace('G#', 'g')
    else:
        return melody


def solution(m, musicinfos):
    answer = [[0] * 2] * 2
    i = 0
    m = change(m)
    for infor in musicinfos:
        music = infor.split(',')
        start = music[0].split(':')
        end = music[1].split(':')
        time = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))
        melody = music[3]
        melody = change(melody)
        melody_played = (melody * time)[:time]

        if m in melody_played:
            answer[i][0] = time
            answer[i][1] = music[2]
        else:
            answer[i][0] = time
            answer[i][1] = "(None)"
        i += 1

        if answer[0][0]




