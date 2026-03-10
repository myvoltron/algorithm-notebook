import sys

sys.setrecursionlimit(10**6)

n = int(input())


def matrix_mul(a, b, m):
    result = [[0, 0], [0, 0]]
    result[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % m
    result[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % m
    result[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % m
    result[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % m
    return result


def recursive_power(matrix, k, m):
    if k == 1:
        return matrix

    half = recursive_power(matrix, k // 2, m)
    half_sqaure = matrix_mul(half, half, m)
    if k % 2 == 0:
        return half_sqaure
    else:
        return matrix_mul(half_sqaure, matrix, m)


def power_iterative(matrix, k, m):
    result = [[1, 0], [0, 1]]
    while k > 0:
        # n의 마지막 비트가 1이면 (홀수면) 현재까지의 a를 곱함
        if k % 2 == 1:
            result = matrix_mul(result, matrix, m)

        # a를 제곱하고 n을 오른쪽으로 시프트 (n // 2)
        matrix = matrix_mul(matrix, matrix, m)
        k //= 2
    return result


base_matrix = [[1, 1], [1, 0]]
# result = recursive_power(base_matrix, n - 1, 1000000007)
result = power_iterative(base_matrix, n - 1, 1000000007)

print(result[0][0])
