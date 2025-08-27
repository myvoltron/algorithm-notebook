import sys

input = sys.stdin.readline

n = int(input())

init = list(map(int, input().split()))
max_result = init
min_result = init
for h in range(n - 1):
    nums = list(map(int, input().split()))

    max_result = [
        max(max_result[0], max_result[1]) + nums[0],
        max(max_result[0], max_result[1], max_result[2]) + nums[1],
        max(max_result[1], max_result[2]) + nums[2],
    ]
    min_result = [
        min(min_result[0], min_result[1]) + nums[0],
        min(min_result[0], min_result[1], min_result[2]) + nums[1],
        min(min_result[1], min_result[2]) + nums[2],
    ]

print(f"{max(max_result)} {min(min_result)}")
