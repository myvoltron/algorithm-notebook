n = int(input())

apart = []
for _ in range(n):
    row = []
    for j in input():
        row.append(int(j))
    apart.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(apart, x, y):
    stack = [(x, y)]

    count = 0
    while stack:
        v = stack.pop()
        if apart[v[0]][v[1]] == 0:
            continue

        apart[v[0]][v[1]] = 0
        count += 1

        for i in range(4):
            r = v[0] + dx[i]
            c = v[1] + dy[i]

            if r >= n or r < 0 or c >= n or c < 0:
                continue
            if apart[r][c] == 0:
                continue

            stack.append((r, c))
    return count


result = []
for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            count = dfs(apart, i, j)
            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i)

