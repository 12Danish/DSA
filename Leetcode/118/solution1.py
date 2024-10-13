class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt = []
        temp = []
        for x in range(numRows):

            if not pt:
                pt.append([1])
                continue

            elif x == 1:
                pt.append([1, 1])
                continue

            else:
                for idx, _ in enumerate(pt[x - 1]):

                    if idx == 0:
                        temp.append(1)

                    else:
                        temp.append(pt[x - 1][idx] + pt[x - 1][idx - 1])

                temp.append(1)
                pt.append(temp)
                temp = []
        return pt


