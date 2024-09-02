# Maximum Subarray

### URL:
[Maximum Sum](https://leetcode.com/problems/maximum-subarray/description/)
## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem requires finding the subarray with the largest sum, which led me to consider an approach that can efficiently track the sum of subarrays while iterating through the array. The key observation is that a subarray with a negative sum would reduce the sum of any future subarray, so it’s better to reset the current sum to zero whenever it becomes negative. This observation aligns with Kadane's algorithm.

## Approach
<!-- Describe your approach to solving the problem. -->
I used Kadane’s algorithm to solve this problem. The algorithm iterates through the array while maintaining a `cur_sum` that stores the sum of the current subarray. If `cur_sum` exceeds the `max_sum`, which tracks the maximum sum encountered so far, we update `max_sum`. If `cur_sum` drops below zero, it is reset to zero because a negative sum would decrease the sum of any subsequent subarray.

## Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $$O(n)$$, where $$n$$ is the number of elements in the array. We iterate through the array once, and each operation within the loop takes constant time.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $$O(1)$$, as we only use a few variables (`max_sum` and `cur_sum`) to store interim results and do not require any additional space proportional to the input size.


## Code
```python3 []
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        cur_sum = 0

        for x in nums:

            cur_sum += x
            if cur_sum > max_sum:
                max_sum = cur_sum

            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum
        
        
```