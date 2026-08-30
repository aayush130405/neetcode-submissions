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
        mapp = {None: None}
        curr = head
        while curr:
            mapp[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            mapp[curr].next = mapp[curr.next]
            mapp[curr].random = mapp[curr.random]
            curr = curr.next
        
        return mapp[head]