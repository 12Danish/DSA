class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        front_xor = {0: 1}
        cur = 0

        for x in A:

            cur = cur ^ x

            if cur ^ B in front_xor:
                count += front_xor[cur ^ B]

            if cur in front_xor:

                front_xor[cur] += 1

            else:
                front_xor[cur] = 1

        return count
