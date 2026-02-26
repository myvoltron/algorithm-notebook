from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n):
    line = list(map(int, input().split()))
    i = 1
    while i < len(line) - 1 or line[i] != -1:
        b = line[i]
        c = line[i + 1]
        tree[line[0]].append((b, c))
        tree[b].append((line[0], c))

        i += 2


def bfs(start):
    q = deque([(start, 0)])
    visited = [False] * (n + 1)
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
