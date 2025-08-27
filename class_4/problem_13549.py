# from collections import deque
#
# n, m = map(int, input().split())
#
# memory = [int(1e9)] * 100001
# memory[n] = 0
#
# q = deque([(n, 0)])
# while q:
#     v = q.popleft()
#
#     if v[0] - 1 >= 0 and memory[v[0] - 1] > v[1] + 1:
#         memory[v[0] - 1] = v[1] + 1
#         q.append((v[0] - 1, v[1] + 1))
#     if v[0] + 1 <= 100000 and memory[v[0] + 1] > v[1] + 1:
#         memory[v[0] + 1] = v[1] + 1
#         q.append((v[0] + 1, v[1] + 1))
#     if v[0] * 2 <= 100000 and memory[v[0] * 2] > v[1]:
#         memory[v[0] * 2] = v[1]
#         q.append((v[0] * 2, v[1]))
#
# print(memory[m])

import heapq

INF = int(1e9)

n, m = map(int, input().split())

distance = [INF] * 100001

q = []
heapq.heappush(q, (0, n))
distance[n] = 0
while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    if now + 1 <= 100000 and distance[now + 1] > dist + 1:
        distance[now + 1] = dist + 1
        heapq.heappush(q, (dist + 1, now + 1))
    if now - 1 >= 0 and distance[now - 1] > dist + 1:
        distance[now - 1] = dist + 1
        heapq.heappush(q, (dist + 1, now - 1))
    if now * 2 <= 100000 and distance[now * 2] > dist:
        distance[now * 2] = dist
        heapq.heappush(q, (dist, now * 2))

print(distance[m])
