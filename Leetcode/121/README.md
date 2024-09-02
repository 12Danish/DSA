# Best Time to Buy and Sell Stock

### URL:
[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The goal is to find the maximum profit possible by buying and selling the stock on different days. The key observation is that we need to find the smallest buying price and the largest selling price after the buying day. A brute-force approach would involve checking every possible pair of buy-sell days, but we can optimize this by iterating through the list and adjusting our buy and sell pointers intelligently.

## Approach
<!-- Describe your approach to solving the problem. -->
I used a two-pointer approach where `buy` starts at index 0 and `sell` starts at index 1. I iterate through the prices while comparing the potential profit from the current `buy` and `sell` pointers:

1. If the difference between `prices[sell]` and `prices[buy]` is negative, it means the `sell` price is lower than the `buy` price, so I move the `buy` pointer forward.
2. If the difference is positive and greater than the current `profit`, I update `profit` with this new value.
3. I always increment the `sell` pointer to move through the list.
4. If `buy` and `sell` become equal after moving the `buy` pointer, the loop continues without unnecessary operations, ensuring we always have distinct days for buying and selling.

This approach ensures that we only need to pass through the list once, making it efficient.

## Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
The time complexity is $$O(n)$$, where $$n$$ is the number of elements in the array. We only iterate through the array once, making it linear time.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
The space complexity is $$O(1)$$, as we only use a few variables (`buy`, `sell`, `profit`) to track the indices and the maximum profit. No additional data structures proportional to the input size are used.

## Code
```python3 []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0

        while buy < len(prices) - 1 and sell < len(prices):
            
            if (prices[sell] - prices[buy]) < 0:
                buy +=1
                if buy != sell:
                    continue
                    
              

            else:
                if(prices[sell] - prices[buy]) > profit:
                    profit =  prices[sell] - prices[buy]
            sell +=1
        
        return profit

```