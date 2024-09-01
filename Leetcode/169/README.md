#  Majority Element

### URL:
[Majority Element](https://leetcode.com/problems/majority-element/description/)

## Approach 1 -> Hashing:

# Intuition
The problem requires finding the majority element in an array, which is defined as the element that appears more than ⌊n / 2⌋ times. To determine this, we can use a hashmap (dictionary) to keep track of the frequency of each element in the array. The majority element will be the one with a frequency greater than or equal to half the size of the array.

# Approach
The approach uses a dictionary (`count`) to store the frequency of each element as we iterate through the array. For each element `x`:
1. If `x` is already in the dictionary, we increment its count.
2. If `x` is not in the dictionary, we add it with an initial count of `1`.
3. During each iteration, we check if the count of the current element is greater than or equal to half the length of the array. If it is, we store this element as the majority element and break out of the loop.

By the end of the iteration, the majority element is the one that satisfies the frequency condition, and we return it.

# Complexity
- Time complexity:  
  The time complexity of this approach is $$O(n)$$ because we iterate through the array once, and dictionary operations (insert and lookup) are average $$O(1)$$.

- Space complexity:  
  The space complexity is $$O(n)$$ because, in the worst case, we might need to store every element in the dictionary.

### Code
```python3 []
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        max_val = None
        ntr = None
        for x in nums:

            if x in count:
                count[x] += 1
            else:
                count[x] = 1

            if x in count and count[x] >= (len(nums) / 2):
                max_val = count[x]
                ntr = x

        return ntr

```
## Approach 2 -> Moore's Voting Algorithm:

### Intuition
The problem asks for the majority element in an array, which is the element that appears more than ⌊n / 2⌋ times. Given that this element must exist, the problem can be solved using a counting method. The intuition is that we can maintain a count while iterating through the array, increasing it when we encounter the same element and decreasing it when we encounter a different one. When the count drops to zero, we start over with the current element as a new candidate.

### Approach
The approach used here is called the **Boyer-Moore Voting Algorithm**. We initialize a candidate (`el`) to `-1` and a counter (`cn`) to `0`. As we iterate through the array:
1. If the counter is `0`, we set the current element as the candidate and reset the counter to `1`.
2. If the current element is the same as the candidate, we increment the counter.
3. If the current element is different from the candidate, we decrement the counter.
This algorithm effectively cancels out pairs of different elements, ensuring that the majority element remains as the candidate by the end of the array.

### Complexity
- Time complexity:  
  The time complexity of this approach is $$O(n)$$ because we only need to iterate through the array once.

- Space complexity:  
  The space complexity is $$O(1)$$ because we are only using a few extra variables (for the candidate and the counter), regardless of the size of the input array.

### Code
```python3 []
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
     
        el = -1
        cn = 0

        for x in nums:

            if cn == 0 : 
                el = x
                cn = 1
                continue

            if x == el :
                cn += 1
            else:
                cn -= 1 
        
        return el

            


         
```