# Longest Subarray with Sum K

### URL:
[Longest Subarray with Sum K](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k)

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
- **Time Complexity**: 
  - The algorithm runs in linear time, so the average time complexity is $$O(n)$$, and the worst case is $$O(n^2)$$ where $$n$$ is the length of the array `arr`.

- **Space Complexity**: 
  - The space complexity is $$O(n)$$ due to the additional space used by the dictionary `sums` to store prefix sums.

## Code

```python
# Your task is to complete this function

class Solution:
    def maxLen(self, arr):
        max_len = 0
        sum_dict = {}
        current_sum = 0

        for idx, num in enumerate(arr):
            current_sum += num

            if current_sum == 0:
                max_len = idx + 1

            elif current_sum in sum_dict:
                max_len = max(max_len, idx - sum_dict[current_sum])

            else:
                sum_dict[current_sum] = idx

        return max_len



