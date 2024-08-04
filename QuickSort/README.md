# Quick Sort Algorithm 

### URL:
[Quick_Sort](https://www.geeksforgeeks.org/quick-sort/)

## General Idea:

Quick sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The key steps are:

- Choose a pivot element from the array.
- Partition the array such that elements less than the pivot are on the left and elements greater than the pivot are on the right.
- Recursively apply the same logic to the left and right sub-arrays.

## Time Complexity:

The time complexity is as follows: $$O(N \log_2 N)$$

## Space Complexity:

The space complexity is as follows: $$O(\log_2 N)$$ due to the recursion stack.
