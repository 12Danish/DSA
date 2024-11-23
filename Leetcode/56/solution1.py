class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final = []
        indices = set()
        ptr1 = 0
        ptr2 = ptr1 + 1
        temp = []
        intervals.sort(key=lambda x: x[0])
        while ptr1 < len(intervals):
            temp = intervals[ptr1]
            ptr2 = ptr1 + 1
            while ptr2 < len(intervals):
                if ptr1 in indices:
                    break

                if ((temp[1] <= intervals[ptr2][1] and temp[1] >= intervals[ptr2][0]) or (
                        temp[1] >= intervals[ptr2][1] and temp[0] <= intervals[ptr2][1])):
                    temp = [min(temp[0], intervals[ptr2][0]), max(temp[1], intervals[ptr2][1])]
                    indices.add(ptr2)
                ptr2 += 1

            if ptr1 not in indices and temp not in final:
                final.append(temp)
                indices.add(ptr1)

            ptr1 += 1

        return final
















