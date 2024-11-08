class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = set()

        for idx, num in enumerate(nums):
            # Skip duplicate values to avoid recalculating
            if idx > 0 and num == nums[idx - 1]:
                continue

            ptr1, ptr2 = idx + 1, len(nums) - 1
            while ptr1 < ptr2:
                sum_value = num + nums[ptr1] + nums[ptr2]

                if sum_value < 0:
                    ptr1 += 1
                elif sum_value > 0:
                    ptr2 -= 1
                else:
                    final.add((num, nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    ptr2 -= 1

                    # Skip duplicates in the inner loop
                    while ptr1 < ptr2 and nums[ptr1] == nums[ptr1 - 1]:
                        ptr1 += 1
                    while ptr1 < ptr2 and nums[ptr2] == nums[ptr2 + 1]:
                        ptr2 -= 1

        return [list(triplet) for triplet in final]
