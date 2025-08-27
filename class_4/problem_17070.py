# dynamic programming
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
#
# dp = [[(0, 0, 0)] * (n + 1) for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     for j in range(3, n + 1):
#         if board[i - 1][j - 1] == 1:
#             dp[i][j] = (0, 0, 0)
#             continue
#
#         if i == 1 and j == 3:
#             dp[i][j] = (1, 0, 0)
#             continue
#         elif i == 2 and j == 3 and (board[0][2] == 0 and board[1][1] == 0):
#             dp[i][j] = (0, 0, 1)
#             continue
#
#         horizontal_value = dp[i][j - 1][0] + dp[i][j - 1][2]
#         vertical_value = dp[i - 1][j][1] + dp[i - 1][j][2]
#         diagonal_value = 0
#         if board[i - 2][j - 1] == 0 and board[i - 1][j - 2] == 0:
#             diagonal_value = (
#                 dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
#             )
#
#         dp[i][j] = (horizontal_value, vertical_value, diagonal_value)
# print(sum(dp[n][n]))

# dfs without recursive
import sys

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


stack = [(0, 1, "H")]
result = 0
while stack:
    x, y, direction = stack.pop()

    if x == n - 1 and y == n - 1:
        result += 1
        continue

    if direction == "H":
        if y + 1 < n and board[x][y + 1] != 1:
            stack.append((x, y + 1, "H"))
        if (
            x + 1 < n
            and y + 1 < n
            and board[x][y + 1] != 1
            and board[x + 1][y] != 1
            and board[x + 1][y + 1] != 1
        ):
            stack.append((x + 1, y + 1, "D"))
    elif direction == "V":
        if x + 1 < n and board[x + 1][y] != 1:
            stack.append((x + 1, y, "V"))
        if (
            x + 1 < n
            and y + 1 < n
            and board[x][y + 1] != 1
            and board[x + 1][y] != 1
            and board[x + 1][y + 1] != 1
        ):
            stack.append((x + 1, y + 1, "D"))
    else:
        if y + 1 < n and board[x][y + 1] != 1:
            stack.append((x, y + 1, "H"))
        if x + 1 < n and board[x + 1][y] != 1:
            stack.append((x + 1, y, "V"))
        if (
            x + 1 < n
            and y + 1 < n
            and board[x][y + 1] != 1
            and board[x + 1][y] != 1
            and board[x + 1][y + 1] != 1
        ):
            stack.append((x + 1, y + 1, "D"))

print(result)
