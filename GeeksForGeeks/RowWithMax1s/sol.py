class Solution:
    def rowWithMax1s(self, arr):

        maxi = -1
        idx1 = -1

        for idx2, row in enumerate(arr):

            low = 0

            high = len(row) - 1

            count = 0

            while low <= high:
                mid = (low + high) // 2
                if row[mid] == 0:

                    low = mid + 1

                elif row[mid] == 1:

                    count = len(row) - mid
                    high = mid - 1

            if count > maxi and count != 0:
                maxi = count

                idx1 = idx2

        return idx1


# {
# Driver Code Starts
# Main execution starts here
if __name__ == "__main__":
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        input_line = input().strip()  # Read input matrix as string
        mat = eval(input_line)  # Convert string to matrix

        solution = Solution()
        result = solution.rowWithMax1s(mat)  # Get the row with the most 1s

        print(result)
        print("~")

# } Driver Code Ends