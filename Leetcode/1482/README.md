Here’s your solution formatted in the requested markdown format:

---

# Minimum Number of Days to Make m Bouquets

### URL:
[Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/)

## Intuition
The problem requires finding the minimum number of days needed to make `m` bouquets, where each bouquet consists of `k` adjacent flowers. The flowers bloom on specific days given by the `bloomDay` array. We need to determine the earliest day when it's possible to pick `m` bouquets, each with `k` adjacent flowers. This can be efficiently solved using a **binary search** approach to find the optimal day.

## Approach
1. **Binary Search Setup**:
   - The minimum possible day is `min(bloomDay)` (the earliest day any flower blooms).
   - The maximum possible day is `max(bloomDay)` (the latest day any flower blooms).

2. **Binary Search Execution**:
   - Perform a binary search between `low = min(bloomDay)` and `high = max(bloomDay)`.
   - For each midpoint `mid`, check if it's possible to make `m` bouquets by day `mid`:
     - Traverse the `bloomDay` array and count the number of adjacent flowers that have bloomed by day `mid`.
     - If `k` adjacent flowers are found, increment the bouquet count and reset the adjacent flower count.
   - If the total number of bouquets `>= m`, it means we can make `m` bouquets by day `mid` or earlier. Update the answer and search for a smaller day (move `high` to `mid - 1`).
   - If the total number of bouquets `< m`, we cannot make `m` bouquets by day `mid`. Search for a larger day (move `low` to `mid + 1`).

3. **Result**:
   - The smallest day that satisfies the condition is returned as the answer. If it's impossible to make `m` bouquets, return `-1`.

## Complexity
- **Time Complexity**:
  - The binary search runs in $$O(\log(\text{max}(bloomDay) - \text{min}(bloomDay)))$$.
  - For each midpoint, we traverse the `bloomDay` array, which takes $$O(n)$$, where `n` is the number of flowers.
  - Overall time complexity: $$O(n \cdot \log(\text{max}(bloomDay) - \text{min}(bloomDay)))$$.

- **Space Complexity**:
  - The algorithm uses constant extra space, so the space complexity is $$O(1)$$.
