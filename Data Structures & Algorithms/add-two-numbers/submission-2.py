# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        
        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            summ = v1 + v2 + carry
            
            carry = summ // 10
            summ = summ % 10
            
            newNode = ListNode(summ)
            tail.next = newNode

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            tail = tail.next
        return dummy.next
            