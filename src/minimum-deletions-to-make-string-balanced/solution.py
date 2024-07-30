class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Create an empty stack to keep track of characters in the string
        stack: list[str] = []

        # Create a counter to keep track of the number of deletions
        delete_count = 0

        # Loop through all characters in `s`
        for character in s:
            if stack and character == "a" and stack[-1] == "b":
                stack.pop()
                delete_count += 1
            else:
                stack.append(character)

        return delete_count
