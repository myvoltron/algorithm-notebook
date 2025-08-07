import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
start = (-1, -1)
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            start = (i, j)
    maps.append(row)

q = deque([start])
visited = [[False for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
while q:
    current = []
    while q:
        v = q.popleft()
        maps[v[0]][v[1]] = count

        for i in range(4):
            x = v[0] + dx[i]
            y = v[1] + dy[i]
            if x >= n or x < 0 or y >= m or y < 0:
                continue
            if maps[x][y] == 0:
                continue
            if visited[x][y]:
                continue

            visited[x][y] = True
            current.append((x, y))
    q.extend(current)
    count += 1

for i in range(n):
    for j in range(m):
        if not visited[i][j] and maps[i][j] != 0:
            print(-1, end=" ")
        else:
            print(maps[i][j], end=" ")
    print()
