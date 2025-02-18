# Sum of Beauty of All Substrings

### URL:
[Sum of Beauty of All Substrings](https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/)

## General Idea:

The problem requires us to find the sum of the beauty values of all possible substrings of a given string `s`. The beauty of a substring is defined as the difference between the highest and lowest frequency of any character in that substring.

### Approach 1 (Brute Force with Substring Storage):
- Generate all possible substrings of `s` and store them in a list.
- For each substring, compute the frequency of each character.
- Find the maximum and minimum frequency values and compute the beauty value.
- Sum up all beauty values to obtain the final result.

### Time Complexity:
- Generating all substrings takes **O(n²)** time.
- Storing substrings takes additional space.
- Frequency computation for each substring takes **O(n)**.
- Overall time complexity: **O(n³)**.

### Space Complexity:
- **O(n²)** for storing substrings.
- **O(1)** additional space for character frequency tracking.

---

### Approach 2 (Optimized Brute Force Without Extra Storage):
- Instead of storing substrings, maintain a frequency dictionary for each starting index.
- Iterate through the string, expanding the substring dynamically.
- Track the maximum and minimum character frequency at each step.
- Sum the beauty values in place.


### Time Complexity:
- Iterating over all substrings: **O(n²)**.
- Frequency computation takes **O(1)** at each step.
- Overall time complexity: **O(n²)** (better than **O(n³)**).

### Space Complexity:
- **O(1)** since the frequency dictionary tracks at most 26 characters.

This optimized approach reduces unnecessary storage and improves efficiency!

