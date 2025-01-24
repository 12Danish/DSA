class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_pos = [-1]
        self.binSearch(0, len(nums) - 1, target, target_pos, nums)
        return target_pos[0]

    def binSearch(self, low, high, target, target_pos, arr):
        if low > high:
            return

        mid = (low + high) // 2

        if arr[mid] == target:
            target_pos[0] = mid
            return

        elif arr[mid] > target:
            if arr[low] > arr[mid] or arr[high] < arr[mid]:
                self.binSearch(mid + 1, high, target, target_pos, arr)
            self.binSearch(low, mid - 1, target, target_pos, arr)

        elif arr[mid] < target:
            if arr[low] > arr[mid] or arr[high] < arr[mid]:
                self.binSearch(low, mid - 1, target, target_pos, arr)
            self.binSearch(mid + 1, high, target, target_pos, arr)
