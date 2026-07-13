function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let currentWeight = 0;

    // 다리 길이만큼 빈 공간 생성
    const queue = Array(bridge_length).fill(0);

    // 대기 트럭 또는 다리 위 트럭이 남아 있는 동안
    while (truck_weights.length > 0 || currentWeight > 0) {
        time += 1;

        // 다리 맨 앞 칸 이동
        const truck = queue.shift();
        currentWeight -= truck;

        // 다음 트럭이 다리에 올라갈 수 있는 경우
        if (
            truck_weights.length > 0 &&
            currentWeight + truck_weights[0] <= weight
        ) {
            const nextTruck = truck_weights.shift();

            queue.push(nextTruck);
            currentWeight += nextTruck;
        } else {
            // 트럭이 못 올라가도 시간은 흐르므로 빈 칸 추가
            queue.push(0);
        }
    }

    return time;
}