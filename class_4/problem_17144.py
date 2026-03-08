r, c, t = map(int, input().split())

board = []
air = []
dusts = []
for i in range(r):
    line = list(map(int, input().split()))
    for j in range(c):
        if line[j] == -1:
            air.append((i, 0))
        if line[j] > 0:
            dusts.append((i, j))
    board.append(line)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while t > 0:
    # dust diffusion
    diffusions = []
    while dusts:
        dust = dusts.pop()
        diffusion_size = board[dust[0]][dust[1]] // 5

        for i in range(4):
            x = dust[0] + dx[i]
            y = dust[1] + dy[i]

            if x >= r or x < 0 or y >= c or y < 0:
                continue
            if board[x][y] == -1:
                continue

            diffusions.append((x, y, diffusion_size))
            diffusions.append((dust[0], dust[1], diffusion_size * -1))

    # diffusion은 한번에 적용
    for diffusion in diffusions:
        x, y, count = diffusion
        board[x][y] += count

    # air
    # top air step
    base_x = air[0][0]
    board[base_x - 1][0] = 0
    for i in range(base_x - 1, 0, -1):
        board[i][0] = board[i - 1][0]
        board[i - 1][0] = 0
    for i in range(1, c):
        board[0][i - 1] = board[0][i]
        board[0][i] = 0
    for i in range(1, base_x + 1):
        board[i - 1][c - 1] = board[i][c - 1]
        board[i][c - 1] = 0
    for i in range(c - 1, 1, -1):
        board[base_x][i] = board[base_x][i - 1]
        board[base_x][i - 1] = 0
    # bottom air step
    base_x = air[1][0]
    board[base_x + 1][0] = 0
    for i in range(base_x + 2, r):
        board[i - 1][0] = board[i][0]
        board[i][0] = 0
    for i in range(1, c):
        board[r - 1][i - 1] = board[r - 1][i]
        board[r - 1][i] = 0
    for i in range(r - 2, base_x - 1, -1):
        board[i + 1][c - 1] = board[i][c - 1]
        board[i][c - 1] = 0
    for i in range(c - 1, 1, -1):
        board[base_x][i] = board[base_x][i - 1]
        board[base_x][i - 1] = 0

    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                dusts.append((i, j))

    t -= 1

# print()
# for i in range(r):
#     for j in range(c):
#         print(board[i][j], end=" ")
#     print()

result = 0
for row in board:
    for item in row:
        if item > 0:
            result += item

print(result)
