class Solution:
    def frequencySort(self, s: str) -> str:

        alphas = {}
        ans = ""
        for char in s:

            if char in alphas:
                alphas[char] += 1

            else:
                alphas[char] = 1

        while alphas:

            max_char = max(alphas, key=alphas.get)

            for x in range(alphas[max_char]):
                ans += max_char

            del alphas[max_char]

        return ans
