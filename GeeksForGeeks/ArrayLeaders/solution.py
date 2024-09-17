class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        leaders = []
        max = arr[n - 1]

        for x in range(n - 1, -1, -1):
            if arr[x] >= max:
                max = arr[x]
                leaders.insert(0, arr[x])

        return leaders
