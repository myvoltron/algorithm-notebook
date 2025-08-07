from collections import deque

n, m = map(int, input().split())


maze = []
for _ in range(n):
    row = []
    for j in input():
        row.append(int(j))
    maze.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr, x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    arr[x][y] = 1

    while q:
        v = q.popleft()

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0 or c >= m or c < 0:
                continue
            if arr[r][c] == 0:
                continue
            if visited[r][c]:
                continue

            q.append((r, c))
            visited[r][c] = True
            arr[r][c] = arr[v[0]][v[1]] + 1


visited = [[False for _ in range(m)] for _ in range(n)]
bfs(maze, 0, 0, visited)
print(maze[-1][-1])
