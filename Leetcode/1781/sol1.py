class Solution:
    def beautySum(self, s: str) -> int:

        als = {}
        subs = []
        beauty = 0
        for x in range(len(s)):

            for y in range(x + 1, len(s) + 1):
                subs.append(s[x: y])

        for sub in subs:

            for let in sub:
                if let not in als:
                    als[let] = 0

                als[let] += 1

            beauty += max(als.values()) - min(als.values())
            als.clear()

        return beauty