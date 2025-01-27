# Find Nth Root of M

### URL:
[Find Nth Root of M](https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-nth-root-of-m)

## Problem Statement:
You are given two numbers, `n` and `m`. The task is to find the nth root of `m` (i.e., \( \sqrt[n]{m} \)). If the root is not an integer, return `-1`.

## General Idea:
The problem requires finding the integer \( x \) such that \( x^n = m \). If no such integer exists, return `-1`. The solution uses a **binary search** approach to efficiently find the nth root.

### Algorithm:
1. **Initialize Search Range:**
   - Set `low` to 1 and `high` to `m`.

2. **Binary Search:**
   - While `low <= high`, calculate the middle value `mid` as `(low + high) // 2`.
   - If `pow(mid, n) == m`, then `mid` is the exact nth root, so return `mid`.
   - If `pow(mid, n) > m`, adjust the search range to the left by setting `high = mid - 1`.
   - If `pow(mid, n) < m`, adjust the search range to the right by setting `low = mid + 1`.

3. **Return Result:**
   - If no exact nth root is found, return `-1`.

## Time Complexity:
The time complexity is **O(log m)** because the binary search halves the search space in each iteration.

## Space Complexity:
The space complexity is **O(1)** as the algorithm uses a constant amount of extra space.

