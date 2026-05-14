from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph = [[-1] * 102 for _ in range(102)]
    visited = [[1] * 102 for _ in range(102)]

    for rect in rectangle:
        x1, y1, x2, y2 = rect[0] * 2, rect[1] * 2, rect[2] * 2, rect[3] * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    q = deque([(characterX, characterY)])
    visited[characterX][characterY] = True

    while q:
        v = q.popleft()

        if v[0] == itemX and v[1] == itemY:
            answer = visited[v[0]][v[1]] // 2
            break

        for i in range(4):
            x = v[0] + dx[i]
            y = v[1] + dy[i]

            if visited[x][y] > 1:
                continue
            if graph[x][y] != 1:
                continue

            visited[x][y] += visited[v[0]][v[1]]
            q.append((x, y))
    return answer 

result = solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
print(result)
