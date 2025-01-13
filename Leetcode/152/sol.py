class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suf = 1
        n = len(nums)
        ans = max(nums)

        for x in range(n):

            if pre == 0:
                pre = 1

            if suf == 0:
                suf = 1

            pre = pre * nums[x]

            suf = suf * nums[n - 1 - x]

            ans = max(ans, pre, suf)

        return ans
