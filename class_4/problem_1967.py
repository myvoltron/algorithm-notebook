# import heapq
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# n = int(input())
#
# graph = [[] for _ in range(n + 1)]
#
# for _ in range(n - 1):
#     a, b, c = map(int, input().split())
#
#     graph[a].append((b, c))
#     graph[b].append((a, c))
#
#
# def dijkstra(start, distance):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
#
# # 임의의 노드에서 가장 먼 곳
# distance = [INF] * (n + 1)
# dijkstra(1, distance)
#
# t_index = 0
# max_t = -1
# for i in range(1, n + 1):
#     if distance[i] > max_t:
#         max_t = distance[i]
#         t_index = i
#
#
# # t 노드에서 가장 먼 곳
# distance = [INF] * (n + 1)
# dijkstra(t_index, distance)
#
# u_index = 0
# max_u = -1
# for i in range(1, n + 1):
#     if distance[i] > max_u:
#         max_u = distance[i]
#         u_index = i
#
# print(max_u)

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))


def bfs(start):
    visited = [False] * (n + 1)

    q = deque([(start, 0)])
    visited[start] = True

    result = [start, 0]

    while q:
        node, dist = q.popleft()

        for i in tree[node]:
            if visited[i[0]]:
                continue

            visited[i[0]] = True
            cost = i[1] + dist
            q.append((i[0], cost))

            if result[1] < cost:
                result = [i[0], cost]

    return result


t = bfs(1)
print(bfs(t[0])[1])
