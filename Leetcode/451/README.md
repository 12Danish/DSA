# Sort Characters By Frequency

### URL:
[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency)

## Intuition
The goal is to sort a given string in decreasing order based on the frequency of its characters. We can achieve this by first counting the occurrences of each character and then constructing the result string in the required order.

## Approach
1. **Count Character Frequencies**:
   - Use a dictionary (`alphas`) to store the frequency of each character in the given string `s`.

2. **Sort Characters by Frequency**:
   - Identify the character with the highest frequency using `max()` with `key=alphas.get`.
   - Append that character to the result string `ans` as many times as it appears in `s`.
   - Remove the processed character from the dictionary.

3. **Repeat Until Dictionary is Empty**:
   - Continue extracting the most frequent character and appending it to `ans` until all characters are processed.

4. **Return the Final String**:
   - The constructed string contains characters sorted in decreasing order of frequency.

## Complexity
- **Time Complexity**:
  - Constructing the frequency dictionary takes **O(n)**.
  - Finding the max frequency character in each iteration takes **O(n)** (in the worst case).
  - Since there are at most **O(n)** iterations, the worst-case complexity is **O(n²)**.
  - Using a heap or sorting instead of `max()` would improve this to **O(n log n)**.

- **Space Complexity**:
  - The dictionary stores at most **O(26) = O(1)** unique characters (for lowercase English letters).
  - The output string requires **O(n)** space.
  - Overall space complexity: **O(n)**.