# 151. Reverse Words in a String

### Url  
[Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

## Intuition  
The problem requires reversing the order of words in a string while ensuring that words are separated by a single space, and any leading/trailing spaces are removed. To solve this efficiently, we iterate through the string from the end to the beginning, extracting words and appending them to the result.

## Approach  
1. Trim leading and trailing spaces from the string.  
2. Initialize variables:
   - `m`: the last index of the trimmed string.
   - `last`: keeps track of the last character of a word.
   - `ans`: stores the reversed words.
   - `space`: a boolean flag to detect spaces.
3. Traverse the string in reverse:
   - If a space is found and `space` is `False`, append the last word to `ans`.
   - If a non-space character is found and `space` is `True`, update `last` to mark a new word.
4. Append the first word manually after the loop.
5. Return the result.

## Complexity  
- **Time Complexity:** $$O(n)$$, where $$n$$ is the length of the string. We traverse the string once.
- **Space Complexity:** $$O(1)$$, as we use a fixed number of variables.

