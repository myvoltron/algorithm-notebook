import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lan = []
for _ in range(k):
    v = int(input())
    lan.append(v)

lan.sort()
left = 0
right = lan[-1]

result = -1
while left <= right:
    mid = (left + right) // 2
    if mid == 0:
        left = mid + 1
        continue

    count = 0
    for i in lan:
        count += i // mid

    if count >= n:
        if result < mid:
            result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
