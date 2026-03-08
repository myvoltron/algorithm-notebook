from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cheese_count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cheese_count += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        v = q.popleft()

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0 or c >= m or c < 0:
                continue
            if visited[r][c]:
                continue
            if board[r][c] == 1:
                continue

            visited[r][c] = True
            q.append((r, c))


result = 0
while cheese_count > 0:
    # 방문한 곳이 외부공간임
    visited = [[False] * m for _ in range(n)]
    bfs(0, 0, visited)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                count = 0
                for k in range(4):
                    r = i + dx[k]
                    c = j + dy[k]

                    if r >= n or r < 0 or c >= m or c < 0:
                        continue

                    if visited[r][c]:
                        count += 1

                if count >= 2:
                    board[i][j] = 0
                    cheese_count -= 1
    result += 1

print(result)
