class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack: list[str] = []
        delete_count = 0

        for character in s:
            if stack and character == "a" and stack[-1] == "b":
                stack.pop()
                delete_count += 1
            else:
                stack.append(character)

        return delete_count
