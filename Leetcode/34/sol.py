class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        low = 0
        high = len(nums) - 1

        self.binSearch(low, high, target, res, nums)
        return res

    def binSearch(self, low, high, target, res, nums):

        if low > high:
            return

        mid = (low + high) // 2

        if nums[mid] == target:

            if res[0] == -1 and res[1] == -1:
                res[0] = mid
                res[1] = mid

            elif mid < res[0]:
                res[0] = mid

            elif mid > res[1]:
                res[1] = mid

            self.binSearch(low, mid - 1, target, res, nums)
            self.binSearch(mid + 1, high, target, res, nums)


        elif nums[mid] > target:

            self.binSearch(low, mid - 1, target, res, nums)

        elif nums[mid] < target:
            self.binSearch(mid + 1, high, target, res, nums)



