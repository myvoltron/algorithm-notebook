import heapq

def solution(jobs):
    # 먼저 작업 요청되는 시점에 따라 오름차순 정렬
    jobs.sort(key=lambda x: x[0])
    answer, time, start, count = 0, 0, 0, 0
    q = []
    while count < len(jobs):
        for job_index in range(start, len(jobs)):
            job = jobs[job_index] # (작업이 요청되는 시점, 작업의 소요시간)
            if job[0] > time:
                break
            heapq.heappush(q, (job[1], job[0]))
            start = job_index + 1
        if q:
            task = heapq.heappop(q)
            count += 1
            time += task[0]
            answer += (time - task[1])
            continue
        time += 1
    return answer // len(jobs)

result = solution([[0, 3], [1, 9], [3, 5]]) # 8
print(result)
