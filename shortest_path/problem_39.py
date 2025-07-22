# 화성 탐사 문제

import heapq

INF = int(1e9)

n = int(input())
square = []
for _ in range(n):
    arr = list(map(int, input().split()))
    square.append(arr)

total_node_num = n * n
graph = [[] for i in range(total_node_num)]
distance = [INF] * total_node_num

for i in range(n):
    for j in range(n):
        current_node = n * i + j
        # left
        if i - 1 > 0:
            graph[current_node].append(((n * (i - 1) + j, square[i - 1][j])))
        # right
        if i + 1 < n:
            graph[current_node].append(((n * (i + 1) + j, square[i + 1][j])))
        # up
        if j - 1 > 0:
            graph[current_node].append(((n * i + (j - 1), square[i][j - 1])))
        # down
        if j + 1 < n:
            graph[current_node].append(((n * i + (j + 1), square[i][j + 1])))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(0)
result = distance[total_node_num - 1] + square[0][0]
print(result)
