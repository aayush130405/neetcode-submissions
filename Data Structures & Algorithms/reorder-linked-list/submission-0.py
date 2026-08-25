# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr2 = slow.next
        prev = None
        slow.next = None

        #2
        while curr2:
            next_node = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = next_node

        #3
        curr = head
        while curr and prev:
            next_list1 = curr.next
            next_list2 = prev.next
            curr.next = prev
            prev.next = next_list1
            curr = next_list1
            prev = next_list2