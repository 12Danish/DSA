# Union of Two Sorted Arrays

### URL:
[Union of Two Sorted Arrays](https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays)

## Intuition
The problem involves finding the union of two sorted arrays, where the union includes all distinct elements that appear in either or both arrays. Given that the arrays are sorted, we can efficiently solve this problem using a two-pointer technique to avoid unnecessary comparisons and ensure that no duplicates are included.

## Approach
1. **Initialization**:
   - Create an empty list `union` to store the union of the two arrays.
   - Initialize two pointers `p1` and `p2` to `0`. These will be used to traverse `arr1` and `arr2` respectively.

2. **Two-Pointer Traversal**:
   - While both `p1` and `p2` are within their respective bounds (`p1 < n` and `p2 < m`):
     - If `arr1[p1]` is equal to `arr2[p2]`, append `arr1[p1]` to `union` only if it's not already the last element in the list (to avoid duplicates). Increment both `p1` and `p2`.
     - If `arr1[p1]` is less than `arr2[p2]`, append `arr1[p1]` to `union` if it’s not a duplicate. Increment `p1`.
     - If `arr1[p1]` is greater than `arr2[p2]`, append `arr2[p2]` to `union` if it’s not a duplicate. Increment `p2`.
   
3. **Handling Remaining Elements**:
   - After the loop, if any elements are left in `arr1`, append them to `union` ensuring no duplicates.
   - Similarly, if any elements are left in `arr2`, append them to `union` ensuring no duplicates.

4. **Helper Function**:
   - The `check_prev` helper function is used to ensure that no element is added to `union` if it’s a duplicate of the last element.

## Complexity
- **Time complexity**: 
  - The algorithm runs in linear time, so the time complexity is $$O(n + m)$$, where $$n$$ and $$m$$ are the lengths of `arr1` and `arr2`, respectively.
  
- **Space complexity**: 
  - The space complexity is $$O(n + m)$$, as we store the union in an additional list.

