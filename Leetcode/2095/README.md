# Delete the Middle Node of a Linked List  

### URL:  
[Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/)  

## General Idea:  

The problem requires deleting the **middle node** from a **singly linked list** and returning the head of the modified list. The middle node is determined using **0-based indexing**, meaning it is located at `⌊n / 2⌋`.  

### Approach:  
- Use **two pointers** (`slow` and `fast`):  
  - `slow` moves **one step** at a time.  
  - `fast` moves **two steps** at a time.  
- When `fast` reaches the end, `slow` will be **just before the middle node**.  
- Adjust the `next` pointer of `slow` to **skip** the middle node.  
- If the list contains only **one node**, return `None`.  

## Time Complexity:  
The time complexity is **O(n)**, as we traverse the list once using the two-pointer approach.  

## Space Complexity:  
The space complexity is **O(1)**, as only a few pointers are used without extra space allocation.  

