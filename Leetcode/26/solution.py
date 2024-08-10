class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {x: 0 for x in nums}
        k = 0
        new_nums = []

        for y in range(len(nums)):
            if count[nums[y]] < 1:
                count[nums[y]] += 1
                new_nums.append(nums[y])
                k += 1

        for i in range(k):
            nums[i] = new_nums[i]

        return k