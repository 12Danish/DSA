class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        maxi = ""

        for x in strs:
            if maxi == "":
                maxi = x
            else:
                maxi = x if len(x) < len(maxi) else maxi

        found = False

        while maxi and not found:
            n = len(maxi)
            found = False

            for y in strs:

                if y[0:n] == maxi:

                    found = True


                else:
                    found = False
                    maxi = maxi[:-1]
                    break

        return maxi


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        maxi = ""

        for x in strs:
            if maxi == "":
                maxi = x
            else:
                maxi = x if len(x) < len(maxi) else maxi

        found = False

        while maxi and not found:
            n = len(maxi)
            found = False

            for y in strs:

                if y[0:n] == maxi:

                    found = True


                else:
                    found = False
                    maxi = maxi[:-1]
                    break

        return maxi


