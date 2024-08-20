class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for x in nums:
            xor = xor ^ x

        return xor