# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        dummy = ListNode(0)
        tail = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                tail = tail.next
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = tail.next
                curr2 = curr2.next
        if curr1 is None:
            while curr2:
                tail.next = curr2
                tail = tail.next
                curr2 = curr2.next
        if curr2 is None:
            while curr1:
                tail.next = curr1
                tail = tail.next
                curr1 = curr1.next
        return dummy.next
        