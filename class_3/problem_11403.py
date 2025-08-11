# INF = int(1e9)
#
# n = int(input())
#
# graph = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     graph.append(row)
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 0:
#             graph[i][j] = INF
#
# for k in range(n):
#     for a in range(n):
#         for b in range(n):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == INF:
#             print(0, end=" ")
#         else:
#             print(1, end=" ")
#     print()

from collections import deque

n = int(input())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


start = deque([])
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            start.append((i, j))

while start:
    v = start.popleft()

    for i in range(n):
        if graph[v[1]][i] == 0:
            continue
        if graph[v[0]][i] == 1:
            continue

        graph[v[0]][i] = 1
        start.append((v[0], i))


for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()
