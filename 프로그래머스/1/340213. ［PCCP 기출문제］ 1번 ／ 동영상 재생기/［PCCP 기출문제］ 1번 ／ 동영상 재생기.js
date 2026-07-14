function solution(video_len, pos, op_start, op_end, commands) {
    const toSeconds = (time) => {
        const [minutes, seconds] = time.split(':').map(Number);
        return minutes * 60 + seconds;
    };

    const toTime = (seconds) => {
        const minutes = Math.floor(seconds / 60);
        const remainSeconds = seconds % 60;

        return (
            String(minutes).padStart(2, '0') +
            ':' +
            String(remainSeconds).padStart(2, '0')
        );
    };

    const videoEnd = toSeconds(video_len);
    const openingStart = toSeconds(op_start);
    const openingEnd = toSeconds(op_end);

    let current = toSeconds(pos);

    const skipOpening = () => {
        if (openingStart <= current && current <= openingEnd) {
            current = openingEnd;
        }
    };

    // 시작부터 오프닝 구간일 수 있음
    skipOpening();

    for (const command of commands) {
        if (command === 'next') {
            current = Math.min(current + 10, videoEnd);
        } else {
            current = Math.max(current - 10, 0);
        }

        skipOpening();
    }

    return toTime(current);
}