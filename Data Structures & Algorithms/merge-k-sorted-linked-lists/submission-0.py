# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#heapq.heappush(heap, item)
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(0)
        tail = dummy
        increase = 0

        for lst in lists:
            if lst:
                increase += 1
                heapq.heappush(heap, (lst.val, increase, lst))
            
        while heap:
            smallestTuple = heapq.heappop(heap)
            smallestNode = smallestTuple[2]

            tail.next = smallestNode
            tail = smallestNode
            if smallestNode.next:
                increase += 1
                heapq.heappush(heap, (smallestNode.next.val, increase, smallestNode.next))

        return dummy.next