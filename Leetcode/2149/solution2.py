class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        new_nums = [None] * len(nums)
        pos_index = 0
        neg_index = 1
        for x in nums:
            if x * 1 >= 0:
                new_nums[pos_index] = x
                pos_index += 2

            else:
                new_nums[neg_index] = x
                neg_index += 2
        return new_nums

        return new_nums
