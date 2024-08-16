class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = (len(nums) * (len(nums) + 1)) // 2

        for x in nums:
            sum -= x

        return sum
