import heapq

INF = float("inf")

n, m, r = map(int, input().split())

# items = [0].extend(list(map(int, input().split())))
items = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


result = -1
for start in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(start, distance)

    current = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
            current += items[i]

    result = max(result, current)

print(result)
