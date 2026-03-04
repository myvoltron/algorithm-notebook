from collections import deque

n = int(input())

board = []
start_position = (0, 0)
fish_position = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 9:
            start_position = (i, j)
            row[j] = 0
        elif row[j] > 0 and row[j] < 9:
            fish_position.append((i, j, row[j]))
    board.append(row)


def bfs(x, y, visited, size, target_x, target_y):
    q = deque([(x, y, 0)])
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        v = q.popleft()

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0 or c >= n or c < 0:
                continue
            if visited[r][c]:
                continue
            if board[r][c] > size:
                continue

            if r == target_x and c == target_y:
                return v[2] + 1

            q.append((r, c, v[2] + 1))
            visited[r][c] = True
    return -1


size = 2
count = 0
result = 0

fish_visited = [False] * len(fish_position)

while True:
    candiates = []

    for i in range(len(fish_position)):
        fish_x, fish_y, fish_size = fish_position[i]
        if fish_size >= size:
            continue
        if fish_visited[i]:
            continue

        visited = [[False] * n for _ in range(n)]
        current_fish_distance = bfs(
            start_position[0], start_position[1], visited, size, fish_x, fish_y
        )

        if current_fish_distance != -1:
            candiates.append((current_fish_distance, fish_x, fish_y, i))
    if not candiates:
        break

    candiates.sort(key=lambda x: (x[0], x[1], x[2]))

    dist, next_x, next_y, fish_index = candiates[0]

    result += dist
    start_position = (next_x, next_y)

    board[next_x][next_y] = 0

    count += 1
    if count == size:
        size += 1
        count = 0

    fish_visited[fish_index] = True

print(result)
