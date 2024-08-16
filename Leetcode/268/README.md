# Missing NUmber

### URL:
[Move Zeroes](https://leetcode.com/problems/missing-number/)

### Intuition
The problem asks to find the missing number in a sequence that contains all numbers from `0` to `n` except one. My first thought was to utilize the property of an arithmetic series, where the sum of the first `n` numbers is given by a simple formula. By calculating the expected sum of the first `n` numbers and then subtracting the sum of the numbers in the array from it, the difference will give the missing number.

### Approach
1. Calculate the expected sum of all numbers from `0` to `n` using the formula `(n * (n + 1)) / 2`.
2. Compute the actual sum of the numbers present in the array.
3. Subtract the sum of the array from the expected sum. The result will be the missing number.

### Complexity
- **Time complexity:** $$O(n)$$  
  We iterate through the array once, which gives us a linear time complexity.

- **Space complexity:** $$O(1)$$  
  We only use a constant amount of extra space for the sum variable, regardless of the input size.

# Code
```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sum = (len(nums)* (len(nums) + 1)) // 2

        for x in nums:
            sum -= x
        
        return sum
        
```