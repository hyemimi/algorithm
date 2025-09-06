function solution(board) {
    const n = board.length;
    const m = board[0].length;
    const dx = [-1,0,1,0];
    const dy = [0,1,0,-1];

    // visited[x][y][dir] = (x,y)에 dir 방향으로 도착했을 때 최소 비용
    const visited = Array.from({length:n}, () => 
        Array.from({length:m}, () => Array(4).fill(Infinity))
    );

    const queue = [];

    // 시작점에서는 오른쪽(1), 아래(2)만 출발 가능
    for (let d of [1,2]) {
        const nx = 0 + dx[d];
        const ny = 0 + dy[d];
        if (0 <= nx && nx < n && 0 <= ny && ny < n && board[nx][ny] === 0) {
            visited[nx][ny][d] = 100;
            queue.push([nx, ny, 100, d]); // x, y, 비용, 방향
        }
    }

    let answer = Infinity;

    while (queue.length > 0) {
        const [x,y,cost,dir] = queue.shift();

        if (x === n-1 && y === m-1) {
            answer = Math.min(answer, cost);
            continue;
        }

        for (let i=0; i<4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] === 0) {
                let newCost = cost + 100;
                if (i !== dir) newCost += 500;

                if (visited[nx][ny][i] > newCost) {
                    visited[nx][ny][i] = newCost;
                    queue.push([nx, ny, newCost, i]);
                }
            }
        }
    }

    return answer;
}
