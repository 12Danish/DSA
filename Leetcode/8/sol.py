class Solution:
    def myAtoi(self, s: str) -> int:

        check = False

        temp = s.strip()

        ans = ""

        for idx, x in enumerate(temp):

            if idx == 0:

                if x == "-":

                    ans += "-"
                    continue

                elif x == "+":
                    continue

            if not check and x == "0":
                continue

            if not check and x.isdigit():
                ans += x
                check = True

                continue

            if check and x.isdigit():
                ans += x
                continue

            break

        try:
            ans = int(ans)

            if ans < -2 ** 31:
                ans = -2 ** 31

            elif ans > 2 ** 31 - 1:
                ans = 2 ** 31 - 1

            return ans

        except:
            return 0











