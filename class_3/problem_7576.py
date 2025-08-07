m, n = map(int, input().split())

tomatoes = []
start = []
for i in range(n):
    cur = list(map(int, input().split()))
    for j in range(m):
        if cur[j] == 1:
            start.append((i, j))
    tomatoes.append(cur)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

while start:
    tmp = []
    while start:
        v = start.pop()
        for i in range(4):
            x = v[0] + dx[i]
            y = v[1] + dy[i]
            if x >= n or x < 0 or y >= m or y < 0:
                continue
            if tomatoes[x][y] == -1 or tomatoes[x][y] == 1:
                continue
            tmp.append((x, y))
            tomatoes[x][y] = 1
    start.extend(tmp)
    result += 1

result -= 1
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            result = -1
            break
print(result)
