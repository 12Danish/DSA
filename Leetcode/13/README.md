# Roman to Integer

### URL:
[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## Problem Statement
Roman numerals are represented by seven different symbols:

| Symbol | Value  |
|--------|--------|
| I      | 1      |
| V      | 5      |
| X      | 10     |
| L      | 50     |
| C      | 100    |
| D      | 500    |
| M      | 1000   |

Roman numerals are usually written from largest to smallest from left to right. However, in certain cases, subtraction is used:

- `I` before `V` or `X` → `IV = 4`, `IX = 9`
- `X` before `L` or `C` → `XL = 40`, `XC = 90`
- `C` before `D` or `M` → `CD = 400`, `CM = 900`

Given a Roman numeral string `s`, convert it to an integer.

## Approach
1. **Initialize `num = 0` and get the length of `s`.**
2. **Iterate through each character in `s`**:
   - If the character is `I`, `X`, or `C`, check the next character to determine if subtraction is needed.
   - Otherwise, add the respective value of the Roman numeral.
3. **Return the final integer value.**

## Complexity
- **Time Complexity**: $$O(n)$$, where $$n$$ is the length of the string.
- **Space Complexity**: $$O(1)$$ since we use only a few integer variables.

