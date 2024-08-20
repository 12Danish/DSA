# 136.Single Number

### Url
[Single Number](https://leetcode.com/problems/single-number/)

## Intuition
The problem states that every element in the array appears twice except for one element. The XOR operation has a property where the XOR of two identical numbers is zero, and the XOR of any number with zero is the number itself. Thus, by XORing all the elements in the array, the elements that appear twice will cancel out, leaving only the single element that appears once.

## Approach
1. Initialize a variable `xor` to 0.
2. Iterate through each element in the array.
3. Perform the XOR operation between `xor` and the current element. This will effectively cancel out any duplicate elements.
4. After the loop, `xor` will contain the single element that does not have a duplicate.
5. Return the value of `xor`.

## Complexity
- Time complexity:
  The time complexity is $$O(n)$$, where $$n$$ is the number of elements in the array. This is because we only need to iterate through the array once.

- Space complexity:
  The space complexity is $$O(1)$$ as no additional space is used that scales with the input size; only a single integer variable is used.
This markdo

## Code
```python3 []
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for x in nums:

            xor = xor ^ x
        
        return xor
```