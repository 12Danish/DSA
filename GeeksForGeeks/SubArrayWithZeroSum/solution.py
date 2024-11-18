# Your task is to complete this function

class Solution:
    def maxLen(self, arr):

        max = 0

        sum_dict = {}

        sum = 0
        for idx, num in enumerate(arr):

            sum += num

            if sum == 0:

                max = idx + 1

            elif sum in sum_dict:

                if idx - sum_dict[sum] > max:
                    max = idx - sum_dict[sum]

            else:

                sum_dict[sum] = idx

        return max

        return max


# {
# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(arr))
        print("~")

# } Driver Code Ends