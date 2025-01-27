# Square Root of a Number

### URL:
[Square Root](https://www.geeksforgeeks.org/problems/square-root/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=square-root)

## General Idea:

The problem requires finding the square root of a given positive integer `n`. If `n` is not a perfect square, the floor value of the square root should be returned. The solution uses a binary search approach to efficiently find the square root.

### Algorithm:

1. **Initialize Search Range:**
   - Set `low` to 1 and `high` to `n`.

2. **Binary Search:**
   - While `low <= high`, calculate the middle value `mid` as `(low + high) // 2`.
   - If `mid * mid == n`, then `mid` is the exact square root, so return `mid`.
   - If `mid * mid > n`, adjust the search range to the left by setting `high = mid - 1`.
   - If `mid * mid < n`, update the answer to `mid` and adjust the search range to the right by setting `low = mid + 1`.

3. **Return Result:**
   - After the loop ends, return the last stored `ans` as the floor value of the square root.

## Time Complexity:

The time complexity is **O(log n)** because the binary search halves the search space in each iteration.

## Space Complexity:

The space complexity is **O(1)** as the algorithm uses a constant amount of extra space.
