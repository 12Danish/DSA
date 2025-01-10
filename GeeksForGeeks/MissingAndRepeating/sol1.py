# User function Template for python3

class Solution:
    def findTwoElement(self, arr):

        nums = set()
        missing = set()
        res = [0, 0]
        for x in range(0, len(arr)):

            if nums and arr[x] in nums:
                res[0] = arr[x]

            else:
                nums.add(arr[x])

        for y in range(1, len(arr) + 1, 1):

            if y not in nums:
                missing.add(y)

        res[1] = min(missing)

        return res


# {
# Driver Code Starts
# Initial Template for Python 3