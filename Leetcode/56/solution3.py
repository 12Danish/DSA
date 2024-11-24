class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return

        n = len(intervals)  # size of the intervalsay

        # sort the given intervals:
        intervals.sort()

        ans = []
        temp = []
        c_start = None
        c_end = None
        temp = [intervals[0][0], intervals[0][1]]
        for i in range(1, n):  # select an interval:

            c_start, c_end = intervals[i][0], intervals[i][1]

            if c_start <= temp[1]:
                temp[1] = max(temp[1], c_end)

            else:
                ans.append(temp)
                temp = [c_start, c_end]

        ans.append(temp)
        return ans

















