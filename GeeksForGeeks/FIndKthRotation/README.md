# Find K Rotation

### URL:
[Find K Rotation](https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation)

## Approach
1. **Overview**:
   - The problem involves finding the number of rotations (`k`) in a sorted and rotated array.
   - The solution uses a **binary search-based approach** to determine the index of the smallest element, which corresponds to the value of `k`.

2. **Steps**:
   - Initialize `num` as a list with one element, `0`, to store the result of rotations.
   - Define a recursive function `binSearch(low, high, arr, num)`:
     - Calculate the middle index `mid` as `(low + high) // 2`.
     - Compare `arr[mid]` with `arr[low]` and `arr[high]`:
       - If `arr[mid] > arr[high]`, the smallest element is to the right of `mid`. Update `num[0]` to `mid + 1`.
       - If `arr[mid] < arr[low]`, the smallest element is at `mid`.
     - Recursively search in both halves of the array.
   - Return `num[0]` as the result, representing the number of rotations.

3. **Complexity Analysis**:
   - **Time Complexity**:
     - The solution divides the search space in half with each recursive call, resulting in \(O(\log n)\) time complexity.
   - **Space Complexity**:
     - The recursion uses the call stack, which takes \(O(\log n)\) space due to the depth of the binary search.



