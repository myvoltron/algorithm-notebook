from collections import deque

n, m = map(int, input().split())

ladders = {}
snakes = {}
while n > 0:
    x, y = map(int, input().split())
    ladders[x] = y
    n -= 1
while m > 0:
    x, y = map(int, input().split())
    snakes[x] = y
    m -= 1

q = deque([1])
board = [0] * 101
while q:
    v = q.popleft()

    for i in range(1, 7):
        next = v + i

        next = snakes.get(next, next)
        next = ladders.get(next, next)

        if next > 100:
            continue
        if board[next] != 0:
            continue
        if board[next] != 0 and board[next] < board[v] + 1:
            continue

        q.append(next)
        board[next] = board[v] + 1

print(board[100])
