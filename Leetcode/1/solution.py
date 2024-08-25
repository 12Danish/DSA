class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {key: idx for idx, key in enumerate(nums)}

        for idx, x in enumerate(nums):
            if target - x in nums_dict and (idx != nums_dict[target - x]):
                return [idx, nums_dict[target - x]]
