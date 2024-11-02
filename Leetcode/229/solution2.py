class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = None
        num2 = None
        cn1 = 0
        cn2 = 0
        final = []

        for x in nums:
            if cn1 == 0 and x != num2:
                num1 = x
                cn1 = 1

            elif cn2 == 0 and x != num1:
                num2 = x
                cn2 = 1

            elif x == num1:
                cn1 += 1

            elif x == num2:
                cn2 += 1

            else:
                cn1 -= 1
                cn2 -= 1

        count1 = sum(1 for x in nums if x == num1)
        count2 = sum(1 for x in nums if x == num2)

        if count1 > len(nums) // 3:
            final.append(num1)
        if count2 > len(nums) // 3 and num2 != num1:
            final.append(num2)

        return final



