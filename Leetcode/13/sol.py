class Solution:
    def romanToInt(self, s: str) -> int:

        num = 0
        length = len(s)

        for idx, x in enumerate(s):

            if x == "I":
                if idx + 1 < length and (s[idx + 1] == "V" or s[idx + 1] == "X"):
                    num -= 1
                else:
                    num += 1

            elif x == "X":
                if idx + 1 < length and (s[idx + 1] == "L" or s[idx + 1] == "C"):
                    num -= 10
                else:
                    num += 10

            elif x == "C":

                if idx + 1 < length and (s[idx + 1] == "D" or s[idx + 1] == "M"):
                    num -= 100
                else:
                    num += 100

            elif x == "V":

                num += 5

            elif x == "L":

                num += 50

            elif x == "D":
                num += 500

            elif x == "M":
                num += 1000

        return num
