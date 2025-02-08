class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []

        prev = 0

        ans = ""

        for idx, x in enumerate(s):

            if x == "(":

                stack.append(x)

            else:

                stack.pop()

            if len(stack) == 0:
                ans += s[prev + 1: idx]
                prev = idx + 1

        return ans