n = int(input())
m = int(input())

target = n + 1

ioi = input()

result = 0
expector = "I"
streak = 0
index = 0
while index < m:
    if expector == "I" and ioi[index] == "I":
        expector = "O"
        streak += 1
    elif expector == "O" and ioi[index] == "O":
        expector = "I"
    elif expector == "I" and ioi[index] == "O":
        if target <= streak:
            result += streak - target + 1
        streak = 0
        expector = "I"
    else:
        if target <= streak:
            result += streak - target + 1
        streak = 1
        expector = "O"

    index += 1
if target <= streak:
    result += streak - target + 1
print(result)
