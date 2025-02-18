class Solution:
    def beautySum(self, s: str) -> int:

        als = {}
        beauty = 0

        for x in range(len(s)):

            als[s[x]] = 1

            for y in range(x + 1, len(s)):

                if not s[y] in als:
                    als[s[y]] = 0

                als[s[y]] += 1
                beauty += max(als.values()) - min(als.values())

            als.clear()

        return beauty