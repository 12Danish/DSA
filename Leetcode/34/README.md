# Find First and Last Position of Element in Sorted Array

### URL:
[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## General Idea:

The problem requires finding the starting and ending positions of a target value in an array sorted in non-decreasing order. If the target value does not exist in the array, return `[-1, -1]`. The solution must have a runtime complexity of $$O(\log n)$$.

### Algorithm:

1. **Binary Search for Target:**
   - Use a recursive binary search function to locate the target value within the range defined by `low` and `high`.

2. **Update Result Array:**
   - If `nums[mid] == target`, update the result array `res`:
     - Set `res[0]` to the minimum of its current value and `mid` (to find the starting position).
     - Set `res[1]` to the maximum of its current value and `mid` (to find the ending position).

3. **Continue Searching:**
   - For the left part of the array, search in the range `[low, mid - 1]`.
   - For the right part of the array, search in the range `[mid + 1, high]`.

4. **Target Not Found:**
   - If the search range becomes invalid (`low > high`), terminate the recursive function.

## Time Complexity:

The time complexity is $$O(\log n)$$ because the solution uses a binary search approach that splits the search range in half at each step.

## Space Complexity:

The space complexity is $$O(\log n)$$ due to the recursive calls of the binary search function.
