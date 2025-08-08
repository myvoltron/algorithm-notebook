from collections import deque

n = int(input())

grid = []
for _ in range(n):
    row = []
    for i in input():
        row.append(i)
    grid.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# color List
def bfs(arr, x, y, visited, color):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        v = q.popleft()

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0 or c >= n or c < 0:
                continue
            if arr[r][c] not in color:
                continue
            if visited[r][c]:
                continue

            visited[r][c] = True
            q.append((r, c))


# not color blindness
not_color_blindness_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            not_color_blindness_count += 1
            bfs(grid, i, j, visited, [grid[i][j]])

# color blindness
color_blindness_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color_blindness_count += 1
            if grid[i][j] == "R" or grid[i][j] == "G":
                bfs(grid, i, j, visited, ["R", "G"])
            else:
                bfs(grid, i, j, visited, ["B"])

print(f"{not_color_blindness_count} {color_blindness_count}")
