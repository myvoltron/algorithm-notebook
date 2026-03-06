from collections import deque

n, m = map(int, input().split())

truths = list(map(int, input().split()))[1:]


person_to_party = [[] for _ in range(51)]
parties = []
for i in range(m):
    party = list(map(int, input().split()))[1:]
    for person in party:
        person_to_party[person].append(i)
    parties.append(party)


def bfs(start, visited):
    q = deque(start)

    while q:
        v = q.popleft()

        for party in person_to_party[v]:
            if visited[party]:
                continue

            visited[party] = True

            for person in parties[party]:
                if person == v:
                    continue
                q.append(person)


visited = [False] * m
bfs(truths, visited)


result = 0
for i in visited:
    if not i:
        result += 1

print(result)
