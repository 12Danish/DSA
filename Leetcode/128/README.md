# Longest Consecutive Sequence

### URL:
[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

### Intuition
The problem requires finding the length of the longest consecutive sequence in an unsorted array, which needs to be done in O(n) time. Using a hash set can help optimize lookups and efficiently check for consecutive elements.

### Approach
1. Convert the input array to a set for O(1) lookups.
2. Iterate through the set and start counting a sequence only when the current number is the start of a sequence (i.e., `x - 1` is not in the set).
3. For each starting number, check for consecutive elements and count the length of the sequence.
4. Keep track of the longest sequence found.

### Complexity
- Time complexity:
  $$O(n)$$ since we only perform constant-time operations for each element in the set.

- Space complexity:
  $$O(n)$$ because we store all elements in a set.


### Code
```python3 []
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) > 0:
            num_set = set()
            for x in nums:
                    num_set.add(x)
            count = 1
            longest = 1
            increment = 1
            for x in num_set:
                if x - 1 in num_set:
                    continue
                continued = True 
                while continued:
                    continued = False
                    if x + increment in num_set:
                        count += 1
                        if count > longest :
                            longest = count
                        increment += 1
                        continued = True
                    
                    else:
                        count = 1
                        increment = 1 
            
            return longest

        else :
            return 0
                    

                


```