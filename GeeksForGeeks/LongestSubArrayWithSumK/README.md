#   Longest Subarray with sum k

### URL:
[Longest Subarray with sum k](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k)

## Approach
1. **Initialization**:
   - Use a dictionary `sums` to store the first occurrence of each prefix sum.
   - Initialize `max_len` to 0, which will store the length of the longest sub-array found.
   - Initialize `sum` to 0 to keep track of the running sum of elements.

2. **Iterate through the array**:
   - For each element `x` in `arr` at index `idx`:
     - Add `x` to `sum`.
     - If `sum == k`, update `max_len` to `idx + 1` because the sub-array from the start to the current index has the sum `k`.
     - If `sum` is not already in `sums`, store `idx` as its first occurrence.
     - Check if `(sum - k)` exists in `sums`. If it does, this means that the sub-array from the index `sums[sum - k] + 1` to `idx` has a sum of `k`. Update `max_len` if this sub-array is longer than the previous one found.

3. **Return Result**:
   - After processing all elements, `max_len` will hold the length of the longest sub-array with sum equal to `k`.

## Complexity
- **Time complexity**: 
  - The algorithm runs in linear time, so the average time complexity is $$O(n)$$,and worst case is  $$O(n * n)$$  where $$n$$ is the length of the array `arr`.

- **Space complexity**: 
  - The space complexity is $$O(n)$$ due to the additional space used by the dictionary `sums` to store prefix sums.







