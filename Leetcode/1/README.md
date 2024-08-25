# Two Sum

### URL:
[Two Sum](https://leetcode.com/problems/two-sum/description/)

# Intuition
The problem requires us to find two numbers in a list that add up to a specific target. The first thought is to use a dictionary to store the numbers and their indices as we iterate through the list. This allows us to efficiently check if the complement of the current number (i.e., `target - current number`) exists in the dictionary.

# Approach
1. Create a dictionary (`nums_dict`) where each key is a number from the list `nums` and its value is the index of that number.
2. Iterate through the list `nums`. For each number `x` at index `idx`, calculate its complement (`target - x`).
3. Check if the complement exists in the dictionary. If it does and the complement's index is not the same as `idx`, return the current index `idx` and the index of the complement.
4. This approach ensures that we find the two numbers that add up to the target in a single pass through the list.

# Complexity
- Time complexity:  
  The time complexity is $$O(n)$$, where $$n$$ is the number of elements in the list. We only iterate through the list once, and dictionary lookups and insertions are average $$O(1)$$ operations.
  
- Space complexity:  
  The space complexity is $$O(n)$$, as we are storing each element of the list along with its index in the dictionary.


# Code
```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {key: idx for idx, key in enumerate(nums)}

        for idx, x in enumerate(nums):
            if target - x in nums_dict and (idx != nums_dict[target - x]):
                return [idx, nums_dict[target - x]]

```