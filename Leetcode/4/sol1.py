class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = []

        p1 = 0

        p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):

            if nums1[p1] <= nums2[p2]:

                merged.append(nums1[p1])
                p1 += 1

            else:
                merged.append(nums2[p2])
                p2 += 1

        while p1 < len(nums1):
            merged.append(nums1[p1])
            p1 += 1

        while p2 < len(nums2):
            merged.append(nums2[p2])
            p2 += 1

        print(merged)

        if (len(merged) - 1) % 2 == 0:

            return merged[(len(merged) - 1) // 2]

        else:

            suma = merged[(len(merged) - 1) // 2] + merged[((len(merged) - 1) // 2) + 1]

            return suma / 2

