class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        low = min(bloomDay)
        high = max(bloomDay)

        ans = -1

        while low <= high:

            mid = (low + high) // 2

            boq = 0
            con = 0

            for day in bloomDay:

                if day <= mid:

                    con += 1

                else:
                    con = 0

                if con == k:
                    boq += 1
                    con = 0

            if boq == m:

                ans = mid
                high = mid - 1

            elif boq < m:
                low = mid + 1

            elif boq > m:

                ans = mid
                high = mid - 1
        return ans

