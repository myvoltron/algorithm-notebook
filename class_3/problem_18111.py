import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

chunk = []
for _ in range(n):
    chunk.append(list(map(int, input().split())))

min_take_time = int(1e9)
max_height = -1
for i in range(257):
    save_blocks = 0
    place_blocks = 0

    for x in range(n):
        for y in range(m):
            if chunk[x][y] > i:
                save_blocks += chunk[x][y] - i
            else:
                place_blocks += i - chunk[x][y]
    if place_blocks > save_blocks + b:
        continue

    current_take_time = place_blocks + save_blocks * 2
    if current_take_time <= min_take_time:
        min_take_time = current_take_time
        max_height = i

print(f"{min_take_time} {max_height}")
