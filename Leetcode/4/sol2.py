class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)

        total_len = m + n

        odd = total_len % 2 == 1

        med = total_len // 2

        el1 = 0
        el2 = 0

        p1 = 0
        p2 = 0

        for x in range(med + 1):

            el1 = el2

            if p1 < m and p2 < n and nums1[p1] <= nums2[p2]:

                el2 = nums1[p1]
                p1 += 1

            elif p1 < m and p2 < n and nums2[p2] < nums1[p1]:

                el2 = nums2[p2]
                p2 += 1

            elif p2 >= n:
                el2 = nums1[p1]
                p1 += 1

            elif p1 >= m:
                el2 = nums2[p2]
                p2 += 1

        if odd:

            return el2

        else:

            return (el1 + el2) / 2

