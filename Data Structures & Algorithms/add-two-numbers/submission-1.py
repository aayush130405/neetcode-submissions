# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        summ = 0
        dummy = ListNode(0)
        tail = dummy

        while curr1 or curr2 or carry:
            if curr1 is None and curr2:
                summ = curr2.val + carry
            elif curr2 is None and curr1:
                summ = curr1.val + carry
            else:
                if curr1 == None and curr2 == None:
                    summ = carry
                else:
                    summ = curr1.val + curr2.val + carry

            if summ >= 10:
                carry = summ // 10
                summ = summ % 10
            else:
                carry = 0
                
            newNode = ListNode(summ)
            tail.next = newNode
            if curr1 != None:
                curr1 = curr1.next
            if curr2 != None:
                curr2 = curr2.next
            tail = tail.next
        return dummy.next
