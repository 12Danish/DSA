# Pascal's Triangle

### URL:
[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)

## Intuition
Pascal's Triangle is a pattern where each element is the sum of the two numbers directly above it, except for the first and last elements of each row which are always 1. The first row is `[1]`, and subsequent rows can be generated by adding adjacent numbers from the previous row. This insight leads us to generate the triangle row by row.

## Approach
1. **Base Case:** Start with the first row as `[1]`.
2. **Row Generation:** For each new row, the first and last elements are always `1`. For the intermediate values, sum the two adjacent elements from the previous row.
3. **Iterate Until numRows:** Continue generating rows until the required number of rows is reached.

## Complexity
- **Time complexity:** $$O(n^2)$$ where $$n$$ is the number of rows. Each row generation involves iterating through the previous row.
- **Space complexity:** $$O(n^2)$$ because we're storing all the rows of Pascal's Triangle in a list of lists.

## Code
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt = []  # Pascal's Triangle
        temp = []  # Temporary list to store the current row

        for x in range(numRows):
            if not pt:
                pt.append([1])  # The first row is always [1]
                continue 
            
            elif x == 1:
                pt.append([1, 1])  # The second row is always [1, 1]
                continue
            
            else:
                for idx, _ in enumerate(pt[x-1]):  # Iterate over the previous row
                    if idx == 0:
                        temp.append(1)  # The first element of each row is 1
                    else:
                        temp.append(pt[x-1][idx] + pt[x-1][idx-1])  # Sum of two adjacent elements
                
                temp.append(1)  # The last element of each row is 1
                pt.append(temp)  # Add the generated row to Pascal's Triangle
                temp = []  # Reset temp for the next row

        return pt
