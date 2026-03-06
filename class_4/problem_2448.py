import sys
import math

n = int(input())
exponent = int(math.log2(int(n // 3)))


m = (2**exponent) * 5 + (2**exponent - 1)
board = [[False] * m for _ in range(n)]


def recursive(depth, x, y):
    if depth == 0:
        board[x][y] = True
        board[x + 1][y - 1] = True
        board[x + 1][y + 1] = True
        board[x + 2][y - 2] = True
        board[x + 2][y - 1] = True
        board[x + 2][y] = True
        board[x + 2][y + 1] = True
        board[x + 2][y + 2] = True
        return

    next_depth = depth - 1
    current = 2**next_depth

    recursive(next_depth, x, y)
    recursive(next_depth, x + (3 * current), y - (3 * current))
    recursive(
        next_depth,
        x + (3 * current),
        y - (3 * current) + (5 * current + 1) + (current - 1),
    )


recursive(exponent, 0, n - 1)

print = sys.stdout.write
for i in range(n):
    for j in range(m):
        if board[i][j]:
            print("*")
        else:
            print(" ")
    print("\n")
