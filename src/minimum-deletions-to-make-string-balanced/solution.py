s = "aababbab"

stack = []
count = 0

for character in s:
    if stack and character == "a" and stack[-1] == "b":
        stack.pop()
        count += 1
    else:
        stack.append(character)


for item in stack:
    print(item)

print(count)
