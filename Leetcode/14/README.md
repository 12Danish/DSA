# Longest Common Prefix

### URL:
[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Intuition
The problem requires us to find the longest common prefix among an array of strings. The naive approach would be to compare every character of every string, but we can optimize it by progressively reducing the prefix until it is common among all strings.

## Approach
1. **Find the shortest string**: The longest possible prefix cannot be longer than the shortest string in the list.
2. **Iterate and check**: Start with the shortest string as the initial prefix. Iterate through all strings and progressively trim the prefix until it matches every string.
3. **Return the longest prefix**: If at any point the prefix becomes empty, return `""`.

