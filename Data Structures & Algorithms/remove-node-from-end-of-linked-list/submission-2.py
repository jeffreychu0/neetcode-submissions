# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        temp = ListNode()
        temp.next = head
        curr = temp
        before_delete = temp
    
        count = n + 1
        while curr:
            curr = curr.next

            if count <= 0:
                before_delete = before_delete.next

            count -= 1

        print(before_delete.val)
        if before_delete.next:
            before_delete.next = before_delete.next.next
        else:
            before_delete.next = None
        return temp.next