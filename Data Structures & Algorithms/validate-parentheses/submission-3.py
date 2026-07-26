class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for bracket in s:
            if bracket in lookup:
                if not stack:
                    return False

                if not stack.pop() == lookup[bracket]:
                    return False
            else:
                stack.append(bracket)

        return not stack