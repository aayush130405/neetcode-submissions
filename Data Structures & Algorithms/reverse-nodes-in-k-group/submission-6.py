# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        prev = None
        while head:
            curr = head
            check = head
            count = 0
            while count < k - 1 and check is not None:
                count += 1
                check = check.next
            if check is None:
                return dummy.next
            nextNode = check.next
            oldHead = head
            while curr is not nextNode:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
            oldHead.next = nextNode
            tail.next = prev
            tail = oldHead

            head = nextNode
            prev = None
        return dummy.next