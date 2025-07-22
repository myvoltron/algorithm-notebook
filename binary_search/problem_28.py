# 고정점 찾기


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid == array[mid]:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        elif array[mid] < mid:
            start = mid + 1
    return None


n = int(input())
sequence = list(map(int, input().split()))

result = binary_search(sequence, 0, len(sequence) - 1)
if result == None:
    print(-1)
else:
    print(result)
