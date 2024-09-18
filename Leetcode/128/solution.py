class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) > 0:
            num_set = set()
            for x in nums:
                num_set.add(x)
            count = 1
            longest = 1
            increment = 1
            for x in num_set:
                if x - 1 in num_set:
                    continue
                continued = True
                while continued:
                    continued = False
                    if x + increment in num_set:
                        count += 1
                        if count > longest:
                            longest = count
                        increment += 1
                        continued = True

                    else:
                        count = 1
                        increment = 1

            return longest

        else:
            return 0




