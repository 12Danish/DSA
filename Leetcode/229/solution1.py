class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_dict = {}
        final = []
        for x in nums:

            if x in num_dict:
                num_dict[x] += 1

            else:
                num_dict[x] = 1

        for key, value in num_dict.items():
            if value > len(nums) / 3:
                final.append(key)

        return final

