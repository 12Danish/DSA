# Row with Maximum 1s

### URL:
[Row with Maximum 1s](https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=row-with-max-1s)

## General Idea:

The problem requires finding the index of the **first row** that contains the **maximum number of 1s** in a **2D binary array** where each row is sorted in **non-decreasing order**. If no such row exists, return `-1`.

## Algorithm:

1. **Iterate Through Each Row:**
   - For each row in the matrix, perform a **binary search** to find the **first occurrence of 1**.

2. **Binary Search to Find the First 1:**
   - Set `low = 0` and `high = len(row) - 1`.
   - Perform binary search:
     - If `row[mid] == 0`, move `low` to `mid + 1` (search right half).
     - If `row[mid] == 1`, update `count` as `len(row) - mid` and move `high` to `mid - 1` (search left half for an earlier occurrence).

3. **Update Maximum Count and Row Index:**
   - If the current row has more `1s` than the previously stored maximum, update `maxi` and store the row index.

4. **Return the Row Index:**
   - If no row contains `1s`, return `-1`.

## Time Complexity:

- **Binary search on each row:** $$O(\log m)$$
- **Iterating through `n` rows:** $$O(n)$$
- **Overall Complexity:** $$O(n \log m)$$

## Space Complexity:

- $$O(1)$$ (constant space, as only a few variables are used)

