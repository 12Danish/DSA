class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)

        total_len = m + n

        odd = total_len % 2 == 1

        arr1 = nums1 if m < n else nums2
        arr2 = nums2 if n > m else nums1

        sym = total_len // 2

        if odd:
            sym += 1

        low = 0
        high = len(arr1)

        while low <= high:

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            mid1 = (low + high) // 2
            mid2 = sym - mid1

            if mid1 - 1 < 0:
                l1 = float('-inf')

            else:
                l1 = arr1[mid1 - 1]

            if mid1 >= len(arr1):
                r1 = float('inf')

            else:
                r1 = arr1[mid1]

            if mid2 - 1 < 0:
                l2 = float('-inf')

            else:
                l2 = arr2[mid2 - 1]

            if mid2 >= len(arr2):
                r2 = float('inf')

            else:
                r2 = arr2[mid2]

            if l1 > r2:

                high = mid1 - 1

            elif r1 < l2:

                low = mid1 + 1

            elif l1 <= r2 and r1 >= l2:
                break

        if odd:

            return max(l1, l2)

        else:

            return (max(l1, l2) + min(r1, r2)) / 2
