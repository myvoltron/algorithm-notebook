import sys

input = sys.stdin.readline

n = int(input())

times = []
for _ in range(n):
    x, y = map(int, input().split())
    times.append((x, y))

times.sort(key=lambda x: (x[1], x[0]))

index = 1
target = times[0][1]
result = 1
while index < n:
    x, y = times[index]
    if target <= x:
        result += 1
        target = y
    index += 1

print(result)
