# Remove Duplicates from Sorted Array

### URL:
[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## General Idea:

The problem requires removing duplicates from a sorted array `nums` in place so that each unique element appears only once. The order of the elements must be maintained, and the function should return the number of unique elements (`k`). The first `k` elements of the modified array should contain the unique elements, while the remaining elements are not important.

- **Create a dictionary `count`:** This dictionary keeps track of how many times each element appears in the array.
- **Initialize `k` and `new_nums`:** `k` keeps track of the count of unique elements, and `new_nums` temporarily stores the unique elements.
- **Iterate through `nums`:** For each element, check if it has been counted before. If not, add it to `new_nums` and increment `k`.
- **Modify `nums`:** Copy the elements from `new_nums` back to the first `k` positions of `nums`.

## Time Complexity:

The time complexity is as follows: $$O(N)$$ because the solution iterates through the list once to build the `new_nums` list and then copies the unique elements to the original `nums` list.

## Space Complexity:

The space complexity is as follows: $$O(N)$$ due to the additional space required for storing the `new_nums` list.
