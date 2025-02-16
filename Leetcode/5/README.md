# Longest Palindromic Substring

### URL:
[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

# Intuition
The problem requires finding the **longest contiguous palindromic substring** in a given string `s`. A palindrome reads the same forward and backward. The goal is to determine the longest such substring efficiently.

A **brute-force approach** generates all possible substrings and checks for palindromes, leading to an **O(n³)** time complexity. Instead, an **expand-around-center approach** reduces this to **O(n²)** by growing potential palindromes outward from each character.

# Approach

### **Approach 1: Brute Force (O(n³) Time, O(n²) Space)**
1. Generate all possible substrings.
2. Check each substring for the palindrome property.
3. Track the longest palindrome found.

This is inefficient due to redundant computations and slow palindrome checking.

---

### **Approach 2: Expand Around Center (O(n²) Time, O(1) Space)**
1. Iterate through each index `i` in `s`.
2. Expand outward from:
   - `s[i]` (odd-length palindromes)
   - `s[i]` and `s[i+1]` (even-length palindromes)
3. Track the longest palindrome found.

This approach efficiently identifies palindromic substrings without storing unnecessary substrings.

# Complexity Comparison

| Approach | Time Complexity | Space Complexity | Explanation |
|----------|---------------|----------------|-------------|
| **Brute Force** | **O(n³)** | **O(n²)** | Generates all substrings and checks for palindromes |
| **Expand Around Center** | **O(n²)** | **O(1)** | Expands outward from each character efficiently |

# Summary
- The brute-force approach is impractical for large `s`.
- **Expand Around Center** is an optimized approach running in **O(n²)**.
- Even more advanced algorithms like **Manacher’s Algorithm** can solve this in **O(n)** time but require additional complexity.
