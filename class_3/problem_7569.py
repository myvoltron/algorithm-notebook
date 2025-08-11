import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

tomato = []
for _ in range(h):
    box = []
    for _ in range(n):
        row = list(map(int, input().split()))
        box.append(row)
    tomato.append(box)

visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque([])
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                q.append((k, i, j))
                visited[k][i][j] = True

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while q:
    v = q.popleft()

    for i in range(6):
        z = v[0] + dz[i]
        r = v[1] + dx[i]
        c = v[2] + dy[i]

        if z >= h or z < 0 or r >= n or r < 0 or c >= m or c < 0:
            continue
        if tomato[z][r][c] == -1:
            continue
        if visited[z][r][c]:
            continue

        tomato[z][r][c] = tomato[v[0]][v[1]][v[2]] + 1
        q.append((z, r, c))
        visited[z][r][c] = True

is_zero_existed = False
result = -1
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0:
                is_zero_existed = True
                break
            if tomato[k][i][j] > result:
                result = tomato[k][i][j]

if not is_zero_existed:
    print(result - 1)
else:
    print(-1)
