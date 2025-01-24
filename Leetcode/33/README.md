# Search in Rotated Sorted Array

### URL:
[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## General Idea:

The problem requires finding the index of a target value in a rotated sorted array. The array was originally sorted in ascending order and then rotated at an unknown pivot index. If the target exists, return its index; otherwise, return `-1`. The solution must achieve a runtime complexity of \(O(\log n)\), which suggests the use of a modified binary search algorithm.

## Approach:

1. **Binary Search:**
   - Identify which part of the array (left or right) is sorted by comparing the middle element with the low and high elements.
   - Decide whether to search in the sorted half or the unsorted half based on the target's value relative to the sorted range.
   - Narrow down the search range by adjusting the `low` and `high` pointers accordingly.

2. **Key Observations:**
   - If the left portion is sorted, check if the target lies within that range.
   - If the right portion is sorted, check if the target lies within that range.
   - Recursively or iteratively repeat until the target is found or the range is exhausted.

## Algorithm:

1. Initialize `low` to 0 and `high` to `len(nums) - 1`.
2. Perform binary search:
   - Calculate `mid` as \((low + high) // 2\).
   - Check if `nums[mid] == target`. If true, return `mid`.
   - Determine which half of the array is sorted:
     - If `nums[low] <= nums[mid]`, the left half is sorted:
       - Check if `target` lies in the range `[nums[low], nums[mid]]`. If yes, adjust `high = mid - 1`. Otherwise, set `low = mid + 1`.
     - Otherwise, the right half is sorted:
       - Check if `target` lies in the range `[nums[mid], nums[high]]`. If yes, adjust `low = mid + 1`. Otherwise, set `high = mid - 1`.
3. If the search range is exhausted, return `-1`.

## Time Complexity:

- **Binary Search:** \(O(\log n)\), since the search space is halved in each iteration.

## Space Complexity:

- \(O(1)\), as the algorithm uses constant space.