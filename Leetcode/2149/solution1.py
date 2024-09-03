class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos = []
        neg = []
        new_nums = []
        for x in nums:
            if x * 1 >= 0:
                pos.append(x)
            else:
                neg.append(x)

        idx1 = 0
        idx2 = 0
        for idx, _ in enumerate(nums):
            if idx % 2 == 0:
                new_nums.append(pos[idx1])
                idx1 += 1
            else:
                new_nums.append(neg[idx2])
                idx2 += 1
        return new_nums
