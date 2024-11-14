class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final: list = []
        i: int = 0
        j: int = i + 1
        k: int = j + 1
        l: int = len(nums) - 1
        while i < len(nums):

            while i < len(nums) and i > 0 and nums[i] == nums[i - 1]:
                i += 1

            j = i + 1
            while j < len(nums):

                while j < len(nums) and j - 1 > i and nums[j] == nums[j - 1]:
                    j += 1

                k = j + 1
                l = len(nums) - 1
                while k < l:

                    while k < l and k - 1 > j and nums[k] == nums[k - 1]:
                        k += 1

                    while l > k and l + 1 < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l -= 1

                    if k < l:
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            final.append([nums[i], nums[j], nums[k], nums[l]])
                            k += 1
                            l -= 1

                        elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                            k += 1

                        elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                            l -= 1
                j += 1
            i += 1
        return final
