class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        thresh_pos = -1

        for idx, num in enumerate(nums):

            for x in range(idx + 1, len(nums)):  # Start from the next number
                if num < nums[x]:
                    # We found a number greater than the current one
                    thresh_pos = idx

                    break

            # Update max if the current num is greater than or equal to remaining elements

        if thresh_pos != -1:
            # Perform the swap with the next largest number
            swap_num = nums[thresh_pos]

            pos_next_max = thresh_pos
            for y in range(thresh_pos + 1, len(nums)):
                if nums[y] > swap_num and (pos_next_max == thresh_pos or nums[y] < nums[pos_next_max]):
                    pos_next_max = y

            self.swap(nums, thresh_pos, pos_next_max)
            self.sort(nums, thresh_pos + 1)
        else:
            # If no valid pair was found, sort the entire array
            self.sort(nums, 0)

    def swap(self, arr, pos1, pos2):
        temp = arr[pos1]
        arr[pos1] = arr[pos2]
        arr[pos2] = temp

    def sort(self, nums, start_idx):
        self.quick_sort(nums, start_idx, len(nums) - 1)

    def quick_sort(self, nums, low, high):

        if low < high:
            m_p = self.partition(nums, low, high)
            self.quick_sort(nums, low, m_p - 1)
            self.quick_sort(nums, m_p + 1, high)

    def partition(self, nums, low, high):

        p_i = low
        l = low
        r = high

        while (l < r):

            while (nums[p_i] >= nums[l] and l < high):
                l += 1
            while (nums[p_i] < nums[r] and r > low):
                r -= 1

            if l < r:
                self.swap(nums, l, r)

        self.swap(nums, p_i, r)

        return r
