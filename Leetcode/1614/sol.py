class Solution:
    def maxDepth(self, s: str) -> int:

        max_val = 0

        stack = []

        for x in s:

            if x == "(":

                stack.append(x)

            elif x == ")":
                stack.pop()

            if len(stack) > max_val:
                max_val = len(stack)

        return max_val

