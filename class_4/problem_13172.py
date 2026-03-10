import sys
import math

input = sys.stdin.readline

n = int(input())
m = 1000000007

numerator = -1
denominator = -1
for i in range(n):
    n, s = map(int, input().split())

    if i == 0:
        numerator = s
        denominator = n
    else:
        numerator = s * denominator + n * numerator
        denominator *= n

gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd


def recursive_power(a, n, m):
    if n == 0:
        return 1

    half = recursive_power(a, n // 2, m)
    if n % 2 == 0:
        return (half * half) % m
    else:
        return (a * half * half) % m


if numerator % denominator == 0:
    print(numerator // denominator)
else:
    # b = pow(denominator, m - 2, m)
    print((numerator * recursive_power(denominator, m - 2, m)) % m)
