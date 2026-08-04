# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)

        curr = temp
        carry_over = False
        while l1 or l2:

            A = l1.val if l1 else 0
            B = l2.val if l2 else 0

            sum_val = A + B

            sum_val += 1 if carry_over else 0
            carry_over = False

            curr.next = ListNode((sum_val) % 10)
            if sum_val >= 10:
                carry_over = True
            else:
                carry_over = False
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry_over:
            curr.next = ListNode(1)

        return temp.next
