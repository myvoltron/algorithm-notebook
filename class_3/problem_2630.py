n = int(input())

color_papers = []
for _ in range(n):
    row = list(map(int, input().split()))
    color_papers.append(row)

blue_papers = 0
white_papers = 0


def recursive(x_start, x_end, y_start, y_end):
    global blue_papers
    global white_papers

    if x_start == x_end and y_start == y_end:
        if color_papers[x_start][y_start] == 1:
            blue_papers += 1
        else:
            white_papers += 1
        return

    # blue first
    is_blue = True
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            if color_papers[i][j] != 1:
                is_blue = False
                break
    # white second
    is_white = True
    for i in range(x_start, x_end + 1):
        for j in range(y_start, y_end + 1):
            if color_papers[i][j] != 0:
                is_white = False
                break

    if is_blue and not is_white:
        blue_papers += 1
        return
    elif is_white and not is_blue:
        white_papers += 1
        return
    else:
        recursive(x_start, (x_start + x_end) // 2, y_start, (y_start + y_end) // 2)
        recursive(x_start, (x_start + x_end) // 2, (y_start + y_end) // 2 + 1, y_end)
        recursive((x_start + x_end) // 2 + 1, x_end, y_start, (y_start + y_end) // 2)
        recursive((x_start + x_end) // 2 + 1, x_end, (y_start + y_end) // 2 + 1, y_end)


blue_papers = 0
white_papers = 0

recursive(0, n - 1, 0, n - 1)

print(white_papers)
print(blue_papers)

