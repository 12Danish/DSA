class Solution:
    def countFreq(self, arr, target):
        freq = [0]
        low = 0
        high = len(arr) - 1

        self.binSearch(low, high, target, freq, arr)
        return freq[0]

    def binSearch(self, low, high, target, freq, arr):

        if low > high:
            return

        mid = (low + high) // 2

        if arr[mid] == target:

            freq[0] += 1

            self.binSearch(low, mid - 1, target, freq, arr)
            self.binSearch(mid + 1, high, target, freq, arr)


        elif arr[mid] > target:

            self.binSearch(low, mid - 1, target, freq, arr)

        elif arr[mid] < target:
            self.binSearch(mid + 1, high, target, freq, arr)



