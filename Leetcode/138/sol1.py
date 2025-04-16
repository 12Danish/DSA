"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        temp = head 
        states = {}

        while temp:

            if temp in states:
                newNode = states[temp]
            
            else:
                newNode =  Node(temp.val)

                states[temp] = newNode 

            if temp.next:
                if temp.next in states:
                    newNext = states[temp.next]
                else:
                    newNext =  Node(temp.next.val)
                    states[temp.next] = newNext

                newNode.next = newNext
            
            if temp.random:
                if temp.random in states:
                    newRandom = states[temp.random]
                else:
                    newRandom =  Node(temp.random.val)
                    states[temp.random] = newRandom

                newNode.random = newRandom
            
            temp = temp.next

        head = states[head]

        return head 
