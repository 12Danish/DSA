class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        subs = []
        ans = ""

        for x in range(0, len(s)):

            for y in range(x + 1, len(s) + 1):
                subs.append(s[x:y])

        if not subs:
            subs.append(s)

        for sub in subs:

            if self.check_pal(sub) and len(sub) > len(ans):
                ans = sub

        return ans

    def check_pal(self, s):
        return s == s[::-1]