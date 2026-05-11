n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = []

start_row = 0
start_column = 0

while True:
    current_max = -1
    max_i = 0
    max_j = 0
    for i in range(start_row, n):
        for j in range(start_column, m):
            if a[i] == b[j]:
                if current_max < a[i]:
                    current_max = a[i]
                    max_i = i
                    max_j = j

    if current_max == -1:
        break
    result.append(current_max)
    start_row = max_i + 1
    start_column = max_j + 1


print(len(result))
if len(result) != 0:
    print(*result)
