
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):

        head = None
        new_node = None
        prev_node = None

        for x in range(len(arr)):

            new_node = Node(arr[x])

            if not head:
                head = new_node

            if prev_node:
                prev_node.next = new_node

            prev_node = new_node


        return head



