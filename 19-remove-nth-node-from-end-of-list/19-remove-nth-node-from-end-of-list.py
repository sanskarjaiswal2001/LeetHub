# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head 
        l = 0
        while temp:
            temp = temp.next
            l += 1
        m = l - n 
        curr = head
        if m == 0:
            head = head.next
            return head
        while m > 0:
            prev = curr
            curr = curr.next
            m -= 1
        prev.next = curr.next
        return head