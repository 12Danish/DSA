# User function Template for python3

class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            p_i = self.partition(arr, low, high)

            self.quickSort(arr, low, p_i - 1)
            self.quickSort(arr, p_i + 1, high)

    # Seelcting a pivot and placing it at its correct position
    def partition(self, arr, low, high):
        p_i = low
        i = low
        j = high

        while i < j:

            while (arr[p_i] >= arr[i] and i < high):
                i += 1

            while (arr[p_i] < arr[j] and j > low):
                j -= 1

            if (i < j):
                self.swap(arr, i, j)

        self.swap(arr, p_i, j)

        return j

    # Performing the swapping
    def swap(self, arr, pos1, pos2):
        temp = arr[pos1]
        arr[pos1] = arr[pos2]
        arr[pos2] = temp

# } Driver Code Ends
