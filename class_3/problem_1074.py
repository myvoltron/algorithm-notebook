n, r, c = map(int, input().split())

size = 2**n

up_left = (0, 0)
up_right = (0, size // 2)
down_left = (size // 2, 0)
down_right = (size // 2, size // 2)
moves = [up_left, up_right, down_left, down_right]

result = 0
while size >= 2:
    current_range = size // 2 - 1
    current_size = size**2 // 4

    for i in range(4):
        if (
            moves[i][0] <= r
            and r <= moves[i][0] + current_range
            and moves[i][1] <= c
            and c <= moves[i][1] + current_range
        ):
            result += current_size * i

            up_left = (moves[i][0], moves[i][1])
            up_right = (
                moves[i][0],
                (moves[i][1] + moves[i][1] + size // 2 - 1) // 2 + 1,
            )
            down_left = (
                (moves[i][0] + moves[i][0] + size // 2 - 1) // 2 + 1,
                moves[i][1],
            )
            down_right = (
                (moves[i][0] + moves[i][0] + size // 2 - 1) // 2 + 1,
                (moves[i][1] + moves[i][1] + size // 2 - 1) // 2 + 1,
            )
            moves = [up_left, up_right, down_left, down_right]
            break

    size //= 2

print(result)
