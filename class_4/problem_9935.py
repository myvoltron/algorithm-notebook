x = input()
y = list(input())

length = len(y)

stack = []
for c in x:
    stack.append(c)

    if stack[-length:] == y:
        for _ in range(length):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
