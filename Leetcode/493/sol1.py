class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = [0]
        self.mergeSort(nums, 0, len(nums) - 1, count)
        return count[0]

    def mergeSort(self, nums, low, high, count):

        if low >= high:
            return

        m = (low + high) // 2

        self.mergeSort(nums, low, m, count)
        self.mergeSort(nums, m + 1, high, count)
        self.merge(nums, low, m, high, count)

    def merge(self, nums, low, m, high, count):

        i = low
        j = m + 1
        temp = []

        while i <= m and j <= high:

            if (i <= m and j <= high and nums[i] <= nums[j]):
                temp.append(nums[i])
                l = j

                while l <= high and nums[i] > 2 * nums[l]:
                    count[0] += 1
                    l += 1

                i += 1

            if (i <= m and j <= high and nums[i] > nums[j]):
                temp.append(nums[j])
                k = i

                if nums[i] > 2 * nums[j]:
                    count[0] += 1 + (m - i)

                else:
                    while (nums[k] <= 2 * nums[j] and k <= m):
                        k += 1
                        if k <= m and nums[k] > 2 * nums[j]:
                            count[0] += 1 + (m - k)
                            break

                j += 1

        while (i <= m):
            temp.append(nums[i])
            i += 1

        while (j <= high):
            temp.append(nums[j])
            j += 1

        for y in range(low, high + 1):
            nums[y] = temp[y - low]


