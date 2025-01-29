---

# Capacity to Ship Packages Within D Days

### URL:
[Capacity to Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

## Intuition
The problem requires finding the minimum weight capacity of a ship to ensure all packages are shipped within `days` days while maintaining the given order. Since we can only load packages in sequence without reordering, we need an efficient way to determine the optimal capacity. This can be solved using **binary search**.

## Approach
1. **Binary Search Setup**:
   - The minimum possible ship capacity is the **heaviest package** (`max(weights)`), as the ship must at least be able to carry the heaviest item.
   - The maximum possible ship capacity is the **sum of all package weights** (`sum(weights)`), which represents the scenario where the ship carries everything in one day.

2. **Binary Search Execution**:
   - Perform a binary search between `low = max(weights)` and `high = sum(weights)`.
   - For each midpoint `mid`, determine how many days it takes to ship all packages with that capacity:
     - Iterate over `weights` and accumulate packages onto the ship until `mid` is exceeded, then count a new day.
   - If the total days `<= days`, it means the capacity is feasible, and we try a smaller value (move `high` to `mid - 1`).
   - If the total days `> days`, it means the capacity is insufficient, and we try a larger value (move `low` to `mid + 1`).

3. **Result**:
   - The smallest `mid` that allows shipping within `days` is returned as the answer.

## Complexity
- **Time Complexity**:
  - The binary search runs in $$O(\log(\sum(\text{weights})))$$.
  - Checking if a capacity is valid takes $$O(n)$$, where `n` is the number of packages.
  - Overall time complexity: $$O(n \cdot \log(\sum(\text{weights})))$$.

- **Space Complexity**:
  - The algorithm uses constant extra space, so the space complexity is $$O(1)$$.
