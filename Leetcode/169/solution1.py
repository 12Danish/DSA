class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_val = None
        ntr = None
        for x in nums:

            if x in count:
                count[x] += 1
            else:
                count[x] = 1

            if x in count and count[x] >= (len(nums) / 2):
                max_val = count[x]
                ntr = x

        return ntr


