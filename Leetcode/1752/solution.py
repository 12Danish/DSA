class Solution:
    def check(self, nums: List[int]) -> bool:
        drop = 0
        for x in range(len(nums)):
            if nums[x] > nums[(x + 1) % len(nums)]:
                drop += 1

        if drop > 1:
            return False

        return True
