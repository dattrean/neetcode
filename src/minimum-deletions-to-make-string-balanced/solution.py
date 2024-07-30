s = "aababbab"

stack = []


for character in s:
    if character and character[-1] == "b" and character == "a":
        stack.pop()
    else:
        stack.append(character)


for item in stack:
    print(item)
