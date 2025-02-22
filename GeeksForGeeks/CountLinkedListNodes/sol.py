# User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''


class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        if not head:
            return 0

        temp = head
        count = 0
        while temp.next:
            temp = temp.next
            count += 1

        count += 1

        return count

