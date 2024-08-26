# Sort Colors

### URL:
[Sort Colors](https://leetcode.com/problems/sort-colors/description/)

# Intuition
The problem is a variation of the classic sorting problem, but with a constraint that we need to sort an array containing only three distinct values (0, 1, and 2) in a specific order. The first thought is to leverage a sorting algorithm that can efficiently handle this specific type of problem.

# Approach
The Dutch National Flag algorithm is ideal for this problem. The algorithm works by maintaining three pointers (`low`, `mid`, and `high`). We start by placing all 0s at the beginning, all 2s at the end, and all 1s will automatically be placed in the middle. The `mid` pointer is used to traverse the array, and depending on the value at `mid`, we either swap with `low` (for 0s) or `high` (for 2s), or move `mid` forward (for 1s).

# Complexity
- Time complexity:  
  $$O(n)$$  
  The algorithm only requires a single pass through the array, making it linear in time.

- Space complexity:  
  $$O(1)$$  
  The sorting is done in place, so the space complexity is constant.


# Code
```python3 []
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0 
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums,low,mid)
                mid += 1
                low += 1
            elif nums[mid] == 1 :
                mid += 1
            elif nums[mid] == 2:
                self.swap(nums,mid,high)
                high -= 1
    
    def swap(self,nums,idx1,idx2):
     
      temp = nums[idx1]
      nums[idx1] = nums[idx2]
      nums[idx2] = temp



        
```