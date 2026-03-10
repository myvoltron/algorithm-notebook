n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


def print_matrix(a):
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()


def matrix_multiplication(a, b):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            item = 0
            for k in range(n):
                item += a[i][k] * b[k][j]
            row.append(item)
        result.append(row)

    return result


def matrix_modulo(a, m):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(a[i][j] % m)
        result.append(row)
    return result


def recursive_power(matrix, k, m):
    if k == 0:
        i = [[0] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if x == y:
                    i[x][y] = 1
        return i

    half = recursive_power(matrix, k // 2, m)
    half_sqaure = matrix_modulo(matrix_multiplication(half, half), m)

    if k % 2 == 0:
        return half_sqaure
    else:
        return matrix_modulo(matrix_multiplication(matrix, half_sqaure), m)


result = recursive_power(matrix, b, 1000)
print_matrix(result)
