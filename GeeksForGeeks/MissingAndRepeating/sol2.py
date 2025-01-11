class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        o_sum = (n * (n + 1)) // 2
        so_sum = (n * (n + 1) * (2 * n + 1)) // 6
        sg_sum = 0
        g_sum = 0

        for x in range(0, len(arr)):
            sg_sum += (arr[x]) * (arr[x])
            g_sum += arr[x]

        diff = g_sum - o_sum

        s_diff = sg_sum - so_sum

        su = s_diff // diff

        rep_num = (su + diff) // 2

        miss_num = su - rep_num

        return [rep_num, miss_num]