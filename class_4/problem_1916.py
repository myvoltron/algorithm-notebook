import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, weight = map(int, input().split())

    graph[start].append((end, weight))

start_point, destination_point = map(int, input().split())

distance = [INF] * (n + 1)

q = []
heapq.heappush(q, (0, start_point))
distance[start_point] = 0

while q:
    dist, v = heapq.heappop(q)

    if distance[v] < dist:
        continue

    for i in graph[v]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (distance[i[0]], i[0]))

print(distance[destination_point])
