n = int(input())

square_nums = [0] * 224
for i in range(1, 224):
    square_nums[i] = i**2

result = 0
while n > 0:
    current_square = 0
    for i in range(223, 0, -1):
        if square_nums[i] <= n:
            current_square = square_nums[i]
            break
    print(f"n -> {n}, current_square->{current_square}")
    n -= current_square
    result += 1

print(result)
