# n, m = map(int, input().split())
#
# grid = []
# for _ in range(n):
#     grid.append(list(input()))
#
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# result = -1
#
#
# def dfs(x, y, depth):
#     global result
#
#     path[ord(grid[x][y]) - ord("A")] = True
#     result = max(result, depth)
#
#     for i in range(4):
#         r = x + dx[i]
#         c = y + dy[i]
#
#         if r >= n or r < 0:
#             continue
#         if c >= m or c < 0:
#             continue
#
#         if path[ord(grid[r][c]) - ord("A")]:
#             continue
#
#         dfs(r, c, depth + 1)
#
#     path[ord(grid[x][y]) - ord("A")] = False
#
#
# path = [False] * 26
# dfs(0, 0, 1)
# print(result)

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(lambda x: ord(x) - 65, input())))


def bfs(x, y):
    s = set([(x, y, 1 << board[x][y], 1)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = -1

    while s:
        v = s.pop()

        result = max(result, v[3])

        if result >= 26:
            return result

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0:
                continue
            if c >= m or c < 0:
                continue

            if v[2] & (1 << board[r][c]):
                continue

            s.add((r, c, v[2] | 1 << board[r][c], v[3] + 1))

    return result


print(bfs(0, 0))
