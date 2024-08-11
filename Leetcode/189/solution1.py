class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        for x in range(len(nums) // 2):
            self.reverse(nums, x, 0)
            x += 1

        for x in range(k // 2):
            self.reverse(nums, x, len(nums) - k)
            x += 1

        for x in range(k, (k + len(nums)) // 2):
            self.reverse(nums, x, -k)
            x += 1

    def reverse(self, nums, x, k):

        print(nums[x])
        print(nums[-1 - x - k])
        nums[x] += nums[-1 - x - k]
        nums[-1 - x - k] = nums[x] - nums[-1 - x - k]
        nums[x] = nums[x] - nums[-1 - x - k]
