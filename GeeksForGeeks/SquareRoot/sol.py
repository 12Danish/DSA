# User function Template for python3


# Complete this function
class Solution:
    def floorSqrt(self, n):

        low = 1
        high = n

        ans = 1

        while low <= high:

            mid = (low + high) // 2

            if mid * mid == n:

                ans = mid
                break

            elif mid * mid > n:

                high = mid - 1

            elif mid * mid < n:

                ans = mid
                low = mid + 1

        return ans

    # {


# Driver Code Starts
# Initial Template for Python 3

