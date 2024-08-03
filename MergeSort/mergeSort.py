# User function Template for python3
class Solution:
    # This function performs the merge
    def merge(self, arr, l, m, r):
        temp = []
        left = l
        right = m + 1
        # Comparing each value, deciding the smalled and adding to the temp
        # this runs until one of the two portions are exhausted
        while left <= m and right <= r:
            if (arr[left] <= arr[right]):
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        # Making sure temp is properly filled
        while (left <= m):
            temp.append(arr[left])
            left += 1

        while (right <= r):
            temp.append(arr[right])
            right += 1
        # Copying temp to main arr
        for x in range(l, r + 1):
            arr[x] = temp[x - l]

    def mergeSort(self, arr, l, r):
        # Base case for recursion
        if l >= r:
            return

        mid = (l + r) // 2

        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge(arr, l, mid, r)
