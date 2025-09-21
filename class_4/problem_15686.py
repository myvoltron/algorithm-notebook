n, m = map(int, input().split())

homes = []
chickens = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            homes.append((i, j))
        elif row[j] == 2:
            chickens.append((i, j))

stack = []
for i in range(len(chickens)):


while stack:
    v = stack.pop()

    for i in range(len(chickens)):
        continue
