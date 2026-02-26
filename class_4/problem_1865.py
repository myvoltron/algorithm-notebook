import sys

input = sys.stdin.readline
INF = int(1e9)


def bf(start, distance, n, m, edges):
    distance[start] = 0

    for _ in range(n + 1):
        for j in range(m):
            a, b, c = edges[j]

            if distance[a] != INF and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c


tc = int(input())

while tc > 0:
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, c * -1))

    distance = [INF] * (n + 1)
    bf(1, distance, n, m + w, edges)

    print(distance)

    tc -= 1
