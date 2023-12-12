name = ["r", "o", "b", "e", "r", "t"]
stack = []
outName = []
for c in name:
    stack.append(c)
for index in range(0, len(stack)):
    print(stack[-1])
    outName.append(stack.pop())

print(outName)