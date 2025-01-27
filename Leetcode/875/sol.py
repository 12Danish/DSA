import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)
        ans = 1

        while low <= high:

            mid = (low + high) // 2

            t_hrs = 0
            for pile in piles:

                t_hrs += math.ceil(pile / mid)

                if t_hrs > h:
                    break

            if t_hrs == h:
                ans = mid
                high = mid - 1



            elif t_hrs > h:
                low = mid + 1


            elif t_hrs < h:
                ans = mid
                high = mid - 1

        return ans