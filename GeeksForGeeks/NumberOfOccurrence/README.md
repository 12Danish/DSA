# Number of Occurrences of Target in Sorted Array

### URL:
[Number of Occurrences](https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-occurrence)

## General Idea:

The problem requires counting the number of occurrences of a given target value in a sorted array `arr[]`. The solution must utilize a binary search approach for efficiency.

### Algorithm:

1. **Binary Search for Target:**
   - Use a recursive binary search function to locate the target value within the array.

2. **Update Frequency:**
   - If `arr[mid] == target`, increment the count stored in `freq`.
   - Continue searching for the target in the left part (`[low, mid - 1]`) and right part (`[mid + 1, high]`) of the array to count all occurrences.

3. **Terminate Search:**
   - If the search range becomes invalid (`low > high`), terminate the recursive function.

4. **Result:**
   - Return the value stored in `freq` as the total count of the target in the array.

## Time Complexity:

The time complexity is $$O(\log n + k)$$, where $$O(\log n)$$ is for locating the target using binary search and $$k$$ is the number of occurrences of the target in the array.

## Space Complexity:

The space complexity is $$O(\log n)$$ due to the recursive calls of the binary search function.
