# 152. Maximum Product Subarray

### Url
[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/)

## Problem
Given an integer array `nums`, find a subarray that has the largest product and return the product.  
The test cases are generated so that the answer will fit in a 32-bit integer.

## Intuition
The maximum product of a subarray can be achieved by either multiplying elements from the left to right or from the right to left. However, a zero can reset the product, so we need to restart the calculation when encountering a zero. By keeping track of both prefix and suffix products, we can ensure that all potential maximum products are considered.

## Approach
1. Initialize two variables, `pre` and `suf`, to 1. These will hold the prefix and suffix products.
2. Initialize `ans` with the maximum value in the array to handle single-element arrays and cases where all elements are negative.
3. Iterate through the array to calculate prefix and suffix products:
   - Multiply `pre` by the current element.
   - Multiply `suf` by the corresponding element from the end of the array.
   - If `pre` or `suf` becomes 0, reset them to 1.
   - Update `ans` with the maximum value of `pre`, `suf`, and `ans`.
4. Return `ans` as the result.

## Complexity
- **Time complexity**:  
  $$O(n)$$, where $$n$$ is the length of the array. This is because we only traverse the array once.

- **Space complexity**:  
  $$O(1)$$, as no additional data structures are used, and only a few integer variables are maintained.