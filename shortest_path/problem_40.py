# 숨바꼭질

import heapq

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    # 양방향
    graph[a].append((b, 1))
    graph[b].append((a, 1))


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


start = 1
dijkstra(start)

max = -1
max_index = 0
for i in range(1, n + 1):
    if distance[i] > max:
        max = distance[i]
        max_index = i

count = 0
for i in range(1, n + 1):
    if distance[i] == max:
        count += 1

print(f"{max_index} {distance[max_index]} {count}")
