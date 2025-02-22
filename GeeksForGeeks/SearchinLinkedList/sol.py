''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:
    def searchKey(self, n, head, key):

        if not head:
            return False

        temp = head

        while temp.next:

            if temp.data == key:
                return True

            temp = temp.next

        if temp.data == key:
            return True

        return False