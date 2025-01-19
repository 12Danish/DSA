# Search Insert Position

### URL:
[Search Insert Position](https://leetcode.com/problems/search-insert-position/)

## General Idea:

The problem requires finding the index of a given target in a sorted array of distinct integers. If the target is not found, the algorithm should return the index where it would be inserted to maintain the sorted order.

### Algorithm:

1. **Initialize Pointers:**
   - Use two pointers, `low` and `high`, to represent the search range. Initialize `low` to 0 and `high` to the last index of the array.

2. **Binary Search:**
   - Calculate the midpoint `mid` using `mid = (low + high) // 2`.
   - Check the value at `nums[mid]`:
     - If `nums[mid] == target`, return `mid`.
     - If `nums[mid] > target`, adjust the search range by setting `high = mid - 1`.
     - If `nums[mid] < target`, adjust the search range by setting `low = mid + 1`.

3. **Return the Insertion Index:**
   - If the target is not found after the binary search loop, `low` will point to the position where the target should be inserted to maintain the sorted order. Return `low`.

## Time Complexity:

The time complexity is $$O(\log n)$$ because the algorithm uses binary search, which repeatedly divides the search space in half.

## Space Complexity:

The space complexity is $$O(1)$$ as the algorithm operates in place without using any additional data structures.
