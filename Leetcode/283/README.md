# Move Zeroes

### URL:
[Move Zeroes](https://leetcode.com/problems/move-zeroes)

## Intuition
The goal is to move all the zeros in the given list to the end while maintaining the relative order of the non-zero elements. The two-pointer approach allows us to achieve this efficiently by minimizing the number of operations and avoiding extra space.

## Approach
1. **Initialization**:
   - We start by initializing a pointer `j` to `-1`. This pointer will help us keep track of the first zero in the list.

2. **First Pass**:
   - We iterate through the list using a pointer `i`. When we encounter the first zero, we set `j` to the index of this zero and break the loop. This `j` pointer will be used to place non-zero elements in subsequent steps.

3. **Second Pass**:
   - We continue iterating through the list starting from `j + 1`. Whenever we find a non-zero element, we place it at the index `j` (the location of the first zero found) and move the zero to the current index `i`.
   - We then increment the `j` pointer to the next index to continue placing subsequent non-zero elements.

4. **Result**:
   - By the end of the iteration, all zeros will have been moved to the end of the list, while the non-zero elements will have been moved to the front in their original relative order.

## Complexity
- Time complexity: 
  - The algorithm runs in a single pass through the list, so the time complexity is $$O(n)$$, where $$n$$ is the number of elements in the list.
  
- Space complexity: 
  - The algorithm uses constant extra space, so the space complexity is $$O(1)$$.
