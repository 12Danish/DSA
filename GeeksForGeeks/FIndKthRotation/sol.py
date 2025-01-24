# User function Template for python3
class Solution:
    def findKRotation(self, arr):
        num = [0]
        self.binSearch(0, len(arr) - 1, arr, num)

        return num[0]

    def binSearch(self, low, high, arr, num):

        if low > high:
            return

        mid = (low + high) // 2

        if arr[mid] > arr[high]:

            num[0] = mid + 1

        elif arr[mid] < arr[low]:

            num[0] = mid

        self.binSearch(mid + 1, high, arr, num)
        self.binSearch(low, mid - 1, arr, num)


# {
# Driver Code Starts
# Initial Template for Python 3

