import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

campus = []
start = (-1, -1)
for i in range(n):
    str = input()
    row = []
    for j in range(m):
        if str[j] == "I":
            start = (i, j)
        row.append(str[j])
    campus.append(row)


def bfs(arr, x, y, visited):
    result = 0
    q = deque([(x, y)])
    visited[x][y] = True

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    while q:
        v = q.popleft()

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0 or c >= m or c < 0:
                continue
            if arr[r][c] == "X":
                continue
            if visited[r][c]:
                continue

            visited[r][c] = True
            if arr[r][c] == "P":
                result += 1

            q.append((r, c))
    return result


visited = [[False for _ in range(m)] for _ in range(n)]
count = bfs(campus, start[0], start[1], visited)
if not count:
    print("TT")
else:
    print(count)
