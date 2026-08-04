# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        length = len(stack)

        curr = head
        for i in range(length // 2):
            temp = curr.next
            curr.next = stack.pop()
            curr = curr.next
            curr.next = temp
            curr = curr.next

        if curr:
            curr.next = None