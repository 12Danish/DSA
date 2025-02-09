class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()

        m = len(s) - 1

        last = m

        ans = ""

        space = False

        for c in range(m, -1, -1):

            if s[c] == " " and not space:

                ans += s[c + 1: last + 1]
                ans += " "
                space = True


            elif s[c] != " " and space:

                last = c
                space = False

        ans += s[0:last + 1]

        return ans




