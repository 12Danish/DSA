# Subarray with Given XOR

### URL:
[Subarray with Given XOR](https://www.interviewbit.com/problems/subarray-with-given-xor/)

# Intuition
The problem requires finding the total number of subarrays whose bitwise XOR equals a given number `B`. The key observation is that for a subarray `A[i:j]`, the XOR of its elements can be expressed as:  
`XOR(A[i:j]) = prefix_xor[j] ^ prefix_xor[i-1]`.  

Rearranging this equation, we get:  
`prefix_xor[i-1] = prefix_xor[j] ^ B`.  

Thus, if we can efficiently check the frequency of `prefix_xor[i-1]` values, we can determine how many subarrays ending at index `j` satisfy the condition. A hashmap (dictionary) is ideal for this purpose as it allows constant time lookups and updates.

# Approach
1. Initialize a dictionary `front_xor` to store the frequency of cumulative XOR values (`prefix_xor`). Start with `front_xor[0] = 1` because XORing with `0` doesn’t change the result.
2. Use a variable `cur` to track the cumulative XOR as you iterate through the array.
3. For each element `x` in the array:
   - Update `cur` by XORing it with `x`.
   - Check if `cur ^ B` exists in `front_xor`. If it does, it means there are subarrays ending at the current index whose XOR equals `B`. Add their count to the result.
   - Update the frequency of `cur` in `front_xor`.
4. Return the total count of subarrays.

# Complexity
- Time complexity:  
  $$O(n)$$, where $$n$$ is the size of the array. We iterate through the array once, and dictionary operations (lookup and update) are average $$O(1)$$.
  
- Space complexity:  
  $$O(n)$$, as we store the cumulative XOR values and their frequencies in the dictionary.

# Code
```python
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        front_xor = {0: 1}
        cur = 0

        for x in A:
            cur ^= x

            # Check if cur ^ B exists in front_xor
            if cur ^ B in front_xor:
                count += front_xor[cur ^ B]

            # Update front_xor with the current cumulative XOR
            if cur in front_xor:
                front_xor[cur] += 1
            else:
                front_xor[cur] = 1

        return count
