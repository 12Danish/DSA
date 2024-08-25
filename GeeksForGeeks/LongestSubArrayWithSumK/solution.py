# User function Template for python3
class Solution:

    def lenOfLongSubarr(self, arr, n, k):

        sums = {}
        max_len = 0
        sum = 0

        for idx, x in enumerate(arr):

            sum += x

            if sum == k:
                max_len = idx + 1

            if sum not in sums:
                sums[sum] = idx

            # Check if (sum - k) exists in the map
            if (sum - k) in sums:
                max_len = max(max_len, idx - sums[sum - k])

        return max_len


