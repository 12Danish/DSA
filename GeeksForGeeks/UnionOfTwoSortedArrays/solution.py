# User function Template for python3

class Solution:

    # Function to return a list containing the union of the two arrays.
    def findUnion(self, arr1, arr2, n, m):

        union = []

        p1 = 0
        p2 = 0

        while p1 < n and p2 < m:

            if arr1[p1] == arr2[p2]:

                if not self.check_prev(union, arr1[p1]):
                    union.append(arr1[p1])
                p1 += 1
                p2 += 1


            elif arr1[p1] < arr2[p2]:

                if not self.check_prev(union, arr1[p1]):
                    union.append(arr1[p1])
                p1 += 1

            elif arr1[p1] > arr2[p2]:

                if not self.check_prev(union, arr2[p2]):
                    union.append(arr2[p2])
                p2 += 1

        while p1 < n:
            if not self.check_prev(union, arr1[p1]):
                union.append(arr1[p1])
            p1 += 1

        while p2 < m:
            if not self.check_prev(union, arr2[p2]):
                union.append(arr2[p2])
            p2 += 1

        return union

    def check_prev(self, arr, num):
        if (arr and arr[-1] == num):
            return True

        return False

# {

# } Driver Code Ends
