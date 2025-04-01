


class Solution:
    def addOne(self, head):

        if not head:
            return

        ans = ""

        temp = head
        lenOr = 0
        while temp:
            ans += str(temp.data)
            temp = temp.next
            lenOr += 1

        ans = int(ans) + 1

        ans = str(ans)
        lenNew = len(ans)

        temp = head

        for idx, num in enumerate(ans):

            if idx == 0 and lenNew > lenOr:
                temp.data = int(str(ans[0]) + str(ans[1]))
                temp = temp.next
                continue

            if idx == 1 and lenNew > lenOr:
                continue

            temp.data = int(num)
            temp = temp.next

        return head

