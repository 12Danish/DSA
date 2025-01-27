Here’s your solution formatted in the requested markdown format:

---

# Koko Eating Bananas

### URL:
[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)

## Intuition
The problem requires finding the minimum eating speed `k` such that Koko can eat all the bananas in `h` hours. Since Koko can choose any pile each hour and eat `k` bananas from it, we need to determine the smallest `k` that allows her to finish all the bananas within the given time constraint. This can be efficiently solved using a **binary search** approach to find the optimal `k`.

## Approach
1. **Binary Search Setup**:
   - The minimum possible eating speed is `1` (eating at least one banana per hour).
   - The maximum possible eating speed is the maximum number of bananas in any pile (`max(piles)`), as eating faster than this won't help.

2. **Binary Search Execution**:
   - Perform a binary search between `low = 1` and `high = max(piles)`.
   - For each midpoint `mid`, calculate the total hours required to eat all the bananas at speed `mid`:
     - For each pile, calculate the hours needed as `math.ceil(pile / mid)`.
     - Sum the hours for all piles.
   - If the total hours `<= h`, it means Koko can eat all the bananas at this speed or slower. Update the answer and search for a smaller `k` (move `high` to `mid - 1`).
   - If the total hours `> h`, Koko cannot finish the bananas at this speed. Search for a larger `k` (move `low` to `mid + 1`).

3. **Result**:
   - The smallest `k` that satisfies the condition is returned as the answer.

## Complexity
- **Time Complexity**:
  - The binary search runs in $$O(\log(\text{max}(piles)))$$.
  - For each midpoint, we calculate the total hours required, which takes $$O(n)$$, where `n` is the number of piles.
  - Overall time complexity: $$O(n \cdot \log(\text{max}(piles)))$$.

- **Space Complexity**:
  - The algorithm uses constant extra space, so the space complexity is $$O(1)$$.
