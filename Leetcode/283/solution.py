class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        if j != -1:
            for i in range(j + 1, len(nums)):
                if nums[i] != 0:
                    nums[j] = nums[i]
                    nums[i] = 0
                    j += 1








