class Solution:
    # User function Template for python3
    # Function to count inversions in the array.
    def inversionCount(self, arr):
        count = [0]
        self.mergeSort(arr, 0, len(arr) - 1, count)

        return count[0]

    def mergeSort(self, arr, low, high, count):

        if low >= high:
            return

        m = (low + high) // 2

        self.mergeSort(arr, low, m, count)
        self.mergeSort(arr, m + 1, high, count)
        self.merge(arr, low, m, high, count)

    def merge(self, arr, low, m, high, count):

        i = low
        j = high
        temp = []

        while i <= m and j > m:

            if (i <= m and j > m and arr[i] <= arr[j]):
                temp.add(arr[i])
                i += 1

            if (i <= m and j > m and arr[i] > arr[j]):
                temp.add(arr[j])
                j -= 1
                count[0] += 1 + (m - i)

        while (i <= m):
            temp.add(arr[i])
            i += 1

        while (j > m):
            temp.add(arr[j])
            j -= 1

        for y in range(low, high):
            arr[y] = temp[y - low]

