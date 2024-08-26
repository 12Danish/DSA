class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, low, mid)
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                self.swap(nums, mid, high)
                high -= 1

    def swap(self, nums, idx1, idx2):

        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp



