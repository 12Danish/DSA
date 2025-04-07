class Solution:
    # Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):

        temp = head

        while temp:

            if temp.data == x:

                if not temp.prev or not temp.next:
                    if not temp.prev and not temp.next:
                        head = None
                        break

                    if not temp.prev:
                        temp = temp.next
                        temp.prev = None
                        head = temp
                        continue

                    if not temp.next:
                        temp.prev.next = None

                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

            temp = temp.next

        return head