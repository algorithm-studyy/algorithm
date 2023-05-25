# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
# 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
# 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
melody_map = {k: v for k, v in zip(['C#', 'D#', 'F#', 'G#', 'A#'], ['c', 'd', 'f', 'g', 'a'])}


def get_diff_minutes(t1, t2):
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    return abs((h1 * 60 + m1) - (h2 * 60 + m2))


def change_melody(melody):
    result = ''
    i = 0
    while i < len(melody):
        if i < len(melody) - 1:
            melody_part = melody[i:i+2]
            if melody_part in melody_map:
                result += melody_map[melody_part]
                i += 2
                continue
        result += melody[i]
        i += 1
    return result


def concat_music(melody, limit):
    result = []
    while len(result) < limit:
        for m in melody:
            if len(result) >= limit:
                return ''.join(result)
            result.append(m)

    return ''.join(result)


def solution(m, musicinfos):
    answer = ''
    m = change_melody(m)
    prev = 0
    for musicinfo in musicinfos:
        t1, t2, music, melody = musicinfo.split(',')
        new_melody = concat_music(change_melody(melody), get_diff_minutes(t1, t2))
        if prev < len(new_melody) and m in new_melody:
            prev = len(new_melody)
            answer = music
    return answer if answer else '(None)'
