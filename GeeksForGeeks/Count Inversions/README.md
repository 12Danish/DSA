# Inversion of Array

### URL:
[Inversion of Array](https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=inversion-of-array)

## Approach
1. **Overview**:
   - The solution involves using the **Merge Sort** technique to count inversions efficiently.
   - Count inversions in the left half, the right half, and during the merging process.

2. **Steps**:
   - Use a recursive `mergeSort` function to divide the array and count inversions.
   - Merge the two halves while counting inversions created during the merge.

3. **Complexity Analysis**:
   - **Time Complexity**:
     - Each division of the array takes \(O(\log n)\), and the merging process takes \(O(n)\). 
     - Therefore, the overall time complexity is \(O(n \log n)\).
   - **Space Complexity**:
     - Additional space is required for the temporary array during the merging process, resulting in \(O(n)\) space complexity.
