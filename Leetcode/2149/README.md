# Rearrange Array Elements by Sign

### URL:
[Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/)

## Approach 1:

### Intuition
To solve this problem, the goal is to rearrange an array such that every consecutive pair of integers have opposite signs. The rearranged array must start with a positive integer, and the order of integers with the same sign should be preserved.

The approach involves separating the positive and negative integers into two lists and then merging them alternately, ensuring that the first element of the final array is positive.

### Approach
1. **Separate Positive and Negative Integers**:
   - Create two lists, `pos` and `neg`, to store positive and negative integers, respectively.
   - Iterate through the `nums` array and append each positive integer to `pos` and each negative integer to `neg`.

2. **Merge Lists Alternately**:
   - Initialize two indices, `idx1` and `idx2`, to keep track of the current position in the `pos` and `neg` lists.
   - Iterate through the `nums` array using an index `idx` and append elements alternately from `pos` and `neg` to the `new_nums` list.
     - If the index is even, append the next positive integer from `pos`.
     - If the index is odd, append the next negative integer from `neg`.

3. **Return the Rearranged Array**:
   - After populating `new_nums` with the elements in the correct order, return the `new_nums` list.

### Complexity
- Time complexity: $$O(n)$$
  - We iterate through the `nums` array twice: once to separate the integers and once to merge them, resulting in a linear time complexity.

- Space complexity: $$O(n)$$
  - We use additional space for the `pos`, `neg`, and `new_nums` lists, which all together require space proportional to the size of the input array.

## Approach 2:

### Intuition
The problem requires rearranging an array such that every consecutive pair of integers has opposite signs, while preserving the relative order of the integers with the same sign. The rearranged array should start with a positive integer.

To solve this, we need to maintain two separate lists for positive and negative integers and then merge them alternately while ensuring the first element is positive.

### Approach
1. **Initialization**:
   - Create a new array `new_nums` with the same length as `nums` to store the rearranged elements.
   - Initialize two indices: `pos_index` to keep track of positions for positive integers (starting at index 0) and `neg_index` for negative integers (starting at index 1).

2. **Iterate through the input array**:
   - For each positive integer in `nums`, place it at the current `pos_index` in `new_nums` and then increment `pos_index` by 2 to maintain alternate positioning.
   - For each negative integer, place it at the current `neg_index` in `new_nums` and then increment `neg_index` by 2 to keep it aligned with the alternating positions.

3. **Return the rearranged array**:
   - After placing all integers in their correct positions, return `new_nums`.

### Complexity
- Time complexity: $$O(n)$$
  - We iterate through the `nums` array once to segregate the integers and place them in the `new_nums` array.

- Space complexity: $$O(n)$$
  - We use an additional array `new_nums` of the same length as the input array to store the rearranged integers.

    