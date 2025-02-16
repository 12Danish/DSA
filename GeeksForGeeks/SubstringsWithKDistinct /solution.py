# User function Template for python3

class Solution:
    def countSubstr(self, s, k):

        def AtMostSub(s, k):

            if k == 0:
                return 0

            count = 0
            ptr1 = 0
            alphas = {}

            for ptr2 in range(len(s)):

                if s[ptr2] not in alphas:
                    alphas[s[ptr2]] = 0

                alphas[s[ptr2]] += 1

                while len(alphas) > k:

                    alphas[s[ptr1]] -= 1

                    if alphas[s[ptr1]] <= 0:
                        del alphas[s[ptr1]]

                    ptr1 += 1

                count += ptr2 - ptr1 + 1

            return count

        return AtMostSub(s, k) - AtMostSub(s, k - 1)

