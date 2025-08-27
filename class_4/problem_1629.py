a, b, c = map(int, input().split())

current = a
result = 1
while b > 0:
    if b % 2 != 0:
        result *= current
        result = result % c
        b -= 1
    elif b % 2 == 0:
        b //= 2
        current = current**2 % c
print(result)


# 10 ** 11
# 10 * 10**10
# 10 * (10**2)**5
# 10 * 4 ** 5
# 10 * 4 * 4**4
# 10 * 4 * (4**2)**2
# 10 * 4 * 4**2
# 10 * 4 * 4
# 10 * 4 * 4 mod 12 = 4
