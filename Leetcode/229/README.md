# Majority Element II

### URL:
[Majority Element II](https://leetcode.com/problems/majority-element-ii/description/)

## General Idea:

The problem requires finding all elements in an integer array `nums` of size `n` that appear more than ⌊ n/3 ⌋ times. The solution needs to be efficient in terms of time and space.

## Approach 1: Dictionary Count

This approach uses a dictionary to store the frequency of each element, then filters the dictionary to identify elements that appear more than ⌊ n/3 ⌋ times.

1. Traverse the array and store each element’s count in a dictionary.
2. Iterate through the dictionary and append elements that appear more than ⌊ n/3 ⌋ times to the result list.

### Time Complexity:

The time complexity is as follows: $$O(N)$$ because we traverse the array once and then iterate through the dictionary.

### Space Complexity:

The space complexity is as follows: $$O(N)$$ due to the dictionary used to store element counts.

## Approach 2: Boyer-Moore Voting Algorithm

This optimized approach uses the Boyer-Moore Voting Algorithm to find potential candidates, then verifies if they appear more than ⌊ n/3 ⌋ times.

1. Initialize two counters (`cn1`, `cn2`) and two candidate variables (`num1`, `num2`).
2. Traverse the array:
   - If a candidate’s counter is zero, set the current element as a new candidate.
   - If the current element matches one of the candidates, increment the respective counter.
   - Otherwise, decrement both counters.
3. After finding the potential candidates, count their occurrences to confirm if they appear more than ⌊ n/3 ⌋ times.

### Time Complexity:

The time complexity is as follows: $$O(N)$$ because we traverse the array twice: once to find potential candidates and once to confirm their counts.

### Space Complexity:

The space complexity is as follows: $$O(1)$$ because only a constant amount of space is used for counters and candidates.
