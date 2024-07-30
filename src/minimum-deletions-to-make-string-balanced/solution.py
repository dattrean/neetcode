s = "aababbab"

stack = []


for character in s:
    if stack and character == "a":
        stack.pop()
    else:
        stack.append(character)


for item in stack:
    print(item)
