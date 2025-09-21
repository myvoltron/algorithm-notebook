from collections import deque

n, m = map(int, input().split())
board = []
virus = []
max_safety_count = 0
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            virus.append((i, j))
        if row[j] == 0:
            max_safety_count += 1
    board.append(row)


def bfs(board, new_walls, start, visited, max_safety_count):
    result = max_safety_count

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for virus in start:
        visited[virus[0]][virus[1]] = True
    result -= 3
    q = deque(start)

    while q:
        v = q.popleft()

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0 or c >= m or c < 0:
                continue
            if board[r][c] == 1:
                continue
            if (r, c) in new_walls:
                continue
            if visited[r][c]:
                continue

            q.append((r, c))
            visited[r][c] = True
            result -= 1
    return result


def comb(arr, r):
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path)
            return
        for i in range(start, len(arr)):
            backtrack(i + 1, path + [arr[i]])

    backtrack(0, [])
    return result


indices_cand = [(r, c) for r in range(n) for c in range(m)]
new_walls = comb(indices_cand, 3)

result = -1
for walls in new_walls:
    visited = [[False] * m for _ in range(n)]
    safety_count = bfs(board, walls, virus, visited, max_safety_count)
    result = max(result, safety_count)
    if safety_count > result:
        result = safety_count

print(result)


# brute force 방식
#
# result = -1
# for i in range(n * m):
#     i_row = i // m
#     i_col = i % m
#     if board[i_row][i_col] == 1 or board[i_row][i_col] == 2:
#         continue
#
#     for j in range(n * m):
#         if j == i:
#             continue
#         j_row = j // m
#         j_col = j % m
#         if board[j_row][j_col] == 1 or board[j_row][j_col] == 2:
#             continue
#
#         for k in range(n * m):
#             if k == j:
#                 continue
#             if k == i:
#                 continue
#             k_row = k // m
#             k_col = k % m
#             if board[k_row][k_col] == 1 or board[k_row][k_col] == 2:
#                 continue
#
#             board[i_row][i_col] = 1
#             board[j_row][j_col] = 1
#             board[k_row][k_col] = 1
#
#             visited = [[False] * m for _ in range(n)]
#             safety_count = bfs(board, virus, visited, max_safety_count)
#             result = max(result, safety_count)
#             if safety_count > result:
#                 result = safety_count
#
#             board[i_row][i_col] = 0
#             board[j_row][j_col] = 0
#             board[k_row][k_col] = 0
#
# print(result)
#

