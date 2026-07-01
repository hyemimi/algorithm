import heapq

def solution(jobs):
    n = len(jobs)
    return_time = [0] * n

    # 요청시간 기준 정렬
    jobs = sorted([(r, d, i) for i, (r, d) in enumerate(jobs)])

    pq = []

    time = 0
    idx = 0      # jobs에서 아직 힙에 안 넣은 작업
    done = 0     # 완료한 작업 수

    while done < n:

        # 현재 시간까지 요청된 작업 모두 힙에 추가
        while idx < n and jobs[idx][0] <= time:
            request, during, num = jobs[idx]
            heapq.heappush(pq, (during, request, num))
            idx += 1

        if pq:
            during, request, num = heapq.heappop(pq)

            time += during
            return_time[num] = time - request
            done += 1
        else:
            # 아직 도착한 작업이 없으면 다음 요청시간으로 이동
            time = jobs[idx][0]

    return sum(return_time) // n