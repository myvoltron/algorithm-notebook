import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for i in range(n):
    weight, value = map(int, input().split())
    graph.append((weight, value))

result = -1
for start in range(n):
    q = deque([(start, graph[start][0], graph[start][1], [start])])

    while q:
        v = q.popleft()
