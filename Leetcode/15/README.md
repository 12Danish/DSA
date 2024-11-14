# 3Sum

### URL
[3Sum](https://leetcode.com/problems/3sum/description/)

## Problem Description
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:
- \(i \neq j\), \(i \neq k\), and \(j \neq k\),
- \( \text{nums[i]} + \text{nums[j]} + \text{nums[k]} = 0 \).

The solution set must not contain duplicate triplets.

## Intuition
The problem requires finding unique triplets in a list that sum up to zero. Sorting the array allows us to use a two-pointer technique to efficiently find pairs that, along with a fixed number, add up to zero. This method helps avoid duplicate triplets and reduces the time complexity.

## Approach
1. **Sort the Array**: Sort `nums` to allow for the two-pointer technique and simplify duplicate handling.
2. **Iterate with a Fixed Element**: For each number at index `i`, treat `nums[i]` as the first element in the triplet.
3. **Two-Pointer Search**: Use two pointers (`left` and `right`) to find pairs that, along with `nums[i]`, sum to zero:
   - If the sum of the three numbers is zero, add the triplet to the result list and move both pointers to find other pairs.
   - If the sum is less than zero, increment the `left` pointer.
   - If the sum is greater than zero, decrement the `right` pointer.
4. **Avoid Duplicates**: Skip over duplicate elements to ensure each triplet is unique.

## Complexity
- **Time Complexity**:  
  \(O(n^2)\), where \(n\) is the number of elements in `nums`. Sorting the array takes \(O(n \log n)\), and the two-pointer search for each fixed element takes \(O(n)\), leading to an overall time complexity of \(O(n^2)\).

- **Space Complexity**:  
  \(O(m)\), where \(m\) is the number of unique triplets. The space is used to store the output list.

## Code
```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
