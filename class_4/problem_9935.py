x = input()
y = input()

length = len(x)

while length > 0:
    x = "".join(x.split(y))
    if length == len(x):
        break
    length = len(x)

if length == 0:
    print("FRULA")
else:
    print(x)
