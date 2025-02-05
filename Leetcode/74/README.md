# Search a 2D Matrix

### URL:
[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

## Approach 1:

### Intuition
Since each row is sorted and the first element of each row is greater than the last element of the previous row, the entire matrix can be visualized as a flattened sorted array. We can apply binary search to achieve an efficient solution.

### Approach
1. **Iterate Through Rows**:
   - Since each row's last element is greater than the first element of the next row, we can skip rows where the last element is smaller than the target.
2. **Binary Search Within the Row**:
   - Perform a standard binary search on the selected row.
   - If the middle element matches the target, return `True`.
   - If the middle element is smaller than the target, search the right half.
   - Otherwise, search the left half.
3. **Return Result**:
   - If no match is found, return `False`.

### Complexity
- **Time Complexity**: $$O(\log(m \times n))$$ because we effectively perform a binary search over the entire matrix.
- **Space Complexity**: $$O(1)$$ since no additional space is used.

