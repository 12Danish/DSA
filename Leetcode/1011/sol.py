class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)

        high = 0

        for weight in weights:
            high += weight

        ans = 0

        while low <= high:

            mid = (low + high) // 2

            c_days = 0
            c_total = 0

            for weight in weights:

                if c_total + weight <= mid:
                    c_total += weight

                else:

                    c_days += 1

                    c_total = weight

                if c_days > days:
                    break

            c_days += 1

            if c_days == days:

                ans = mid
                high = mid - 1

            elif c_days > days:

                low = mid + 1

            elif c_days < days:
                ans = mid
                high = mid - 1

        return ans








