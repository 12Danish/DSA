class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        ans = ""

        def check_pal(s, left, right):

            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        for i in range(len(s)):
            odd_pal = check_pal(s, i, i)
            even_pal = check_pal(s, i, i + 1)
            ans = max(ans, odd_pal, even_pal, key=len)

        return ans