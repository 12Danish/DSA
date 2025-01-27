# User function Template for python3

class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        low = 1
        high = m
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if pow(mid, n) == m:
                ans = mid
                break
            elif pow(mid, n) > m:
                high = mid - 1
            elif pow(mid, n) < m:  # Fixed: Changed `n` to `m`

                low = mid + 1

        return ans


