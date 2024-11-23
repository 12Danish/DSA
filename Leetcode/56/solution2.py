class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)  # size of the intervalsay

        # sort the given intervals:
        intervals.sort()

        ans = []

        for i in range(n):  # select an interval:
            start, end = intervals[i][0], intervals[i][1]

            # Skip all the merged intervals:
            if ans and end <= ans[-1][1]:
                continue

            # check the rest of the intervals:
            for j in range(i + 1, n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start, end])
        return ans




