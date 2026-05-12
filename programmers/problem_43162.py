from collections import deque


def solution(n, computers):
    def bfs(start, visited):
        q = deque([start])
        visited[start] = True

        while q:
            v = q.popleft()

            for index in range(n):
                if index == v:
                    continue
                if visited[index]:
                    continue
                if computers[v][index] == 0:
                    continue

                visited[index] = True
                q.append(index)

    visited = [False] * n
    count = 0
    answer = 0
    for start in range(n):
        bfs(start, visited)
        if count < visited.count(True):
            count = visited.count(True)
            answer += 1
    return answer


# result = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
result = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
print(result)
