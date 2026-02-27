from itertools import combinations

n, m = map(int, input().split())

homes = []
chickens = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            homes.append((i, j))
        elif line[j] == 2:
            chickens.append((i, j))


def cal_distance(home, chicken):
    return abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])


distance = []
for h in homes:
    row = []
    for c in chickens:
        row.append(cal_distance(h, c))
    distance.append(row)

result = float("inf")
for comb in combinations(range(len(chickens)), m):
    current = 0
    for h in distance:
        chicken_distance = int(1e9)
        for c in comb:
            chicken_distance = min(chicken_distance, h[c])
        current += chicken_distance
    result = min(result, current)

print(result)
