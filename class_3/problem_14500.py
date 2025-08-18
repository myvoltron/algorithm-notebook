n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

# brute force
# tetromino_row = [
#     [0, 0, 0, 0],
#     [0, 0, 1, 1],
#     [0, 0, -1, -2],
#     [0, 0, -1, -2],
#     [0, 1, 1, 2],
#     [0, 1, 1, 2],
#     [0, 0, 0, 1],
#     [0, 0, 0, -1],
# ]
# tetromino_column = [
#     [0, 1, 2, 3],
#     [0, 1, 0, 1],
#     [0, -1, -1, -1],
#     [0, 1, 1, 1],
#     [0, 0, 1, 1],
#     [0, 0, -1, -1],
#     [0, 1, 2, 1],
#     [0, 1, 2, 1],
# ]
#
#
# def calc_sum(arr, row, column, tetromino_dx, tetromino_dy):
#     result = -1
#     for _ in range(4):
#         current_sum = 0
#         is_normal = True
#         for k in range(4):
#             x = row + tetromino_dx[k]
#             y = column + tetromino_dy[k]
#             if x >= n or x < 0 or y >= m or y < 0:
#                 is_normal = False
#                 break
#             current_sum += arr[x][y]
#
#         if is_normal:
#             result = max(result, current_sum)
#
#         # rotate
#         tetromino_dx, tetromino_dy = tetromino_dy, tetromino_dx
#         tetromino_dy = list(map(lambda x: x * -1, tetromino_dy))
#     return result
#
#
# result = -1
# for i in range(n):
#     for j in range(m):
#         for k in range(8):
#             result = max(
#                 result,
#                 calc_sum(arr, i, j, tetromino_row[k], tetromino_column[k]),
#             )
# print(result)


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # x, y, depth, sum, visited
    s = [(x, y, 0, arr[x][y], [(x, y)])]

    result = 0
    while s:
        v = s.pop()

        if v[2] == 3:
            result = max(result, v[3])
            continue

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0 or c >= m or c < 0:
                continue
            if (r, c) in v[4]:
                continue

            s.append((r, c, v[2] + 1, v[3] + arr[r][c], v[4] + [(r, c)]))
    return result


def calculate_t_shape(x, y):
    dx = [0, 0, 0, -1]
    dy = [0, 1, 2, 1]

    result = 0
    for _ in range(4):
        current = 0
        for k in range(4):
            r = x + dx[k]
            c = y + dy[k]
            if r >= n or r < 0 or c >= m or c < 0:
                current = 0
                break
            current += arr[r][c]
        result = max(result, current)

        # rotate
        dx, dy = dy, dx
        dy = list(map(lambda x: x * -1, dy))

    return result


result = 0
for i in range(n):
    for j in range(m):
        result = max(result, dfs(i, j), calculate_t_shape(i, j))


print(result)
