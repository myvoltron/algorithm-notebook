import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


memory = [0] * (n + 1)
visited = [False] * (n + 1)

q = deque([(1, tree[1])])
visited[1] = True

while q:
    v = q.popleft()

    for node in v[1]:
        if visited[node]:
            continue

        visited[node] = True
        memory[node] = v[0]

        q.append((node, tree[node]))


for i in range(2, n + 1):
    print(memory[i])
