# Check If Array Is Sorted and Rotated

### URL:
[Check If Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/submissions/1349241916/)

## General Idea:

The problem checks whether a given array can be represented as a sorted array that has been rotated. The approach involves counting the number of "drops" in the array, which are points where an element is greater than the next one. If there is more than one drop, the array cannot be a valid rotated sorted array.

- Iterate through the array and compare each element with the next one.
- Use modulo operation to handle the circular nature of rotation.
- Count the number of drops where an element is greater than the next.
- If there is more than one drop, the array is not a rotated sorted array.

## Time Complexity:

The time complexity is as follows: $$O(N)$$

## Space Complexity:

The space complexity is as follows: $$O(1)$$ since the algorithm only uses a constant amount of extra space.
