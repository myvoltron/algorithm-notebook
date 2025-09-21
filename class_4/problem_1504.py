import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

required_x, required_y = map(int, input().split())

INF = float("inf")


def dijkstra(start, end):
    distance = [INF] * (n + 1)
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

    return distance[end]


# 1 -> a -> b -> n
# 1 -> b -> a -> n
result = min(
    dijkstra(1, required_x)
    + dijkstra(required_x, required_y)
    + dijkstra(required_y, n),
    dijkstra(1, required_y)
    + dijkstra(required_y, required_x)
    + dijkstra(required_x, n),
)
if result >= INF:
    print(-1)
else:
    print(result)
