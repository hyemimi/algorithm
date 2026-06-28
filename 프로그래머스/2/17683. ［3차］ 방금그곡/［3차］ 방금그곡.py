def solution(m, musicinfos):
    answer = "(None)"
    maxTime = -1

    m = convert(m)

    for music in musicinfos:
        start, end, title, melody = music.split(',')

        melody = convert(melody)

        startHour, startMinute = map(int, start.split(':'))
        endHour, endMinute = map(int, end.split(':'))

        startMinutes = startHour * 60 + startMinute
        endMinutes = endHour * 60 + endMinute

        diff = endMinutes - startMinutes

        # 재생된 시간만큼 멜로디 문자열 생성
        target = ""
        for i in range(diff):
            target += melody[i % len(melody)]

        # 재생된 시간이 가장 긴 시간 선택
        if m in target:
            if diff > maxTime:
                maxTime = diff
                answer = title

    return answer


def convert(melody):
    return (melody.replace("C#", "c")
                  .replace("D#", "d")
                  .replace("F#", "f")
                  .replace("G#", "g")
                  .replace("A#", "a"))