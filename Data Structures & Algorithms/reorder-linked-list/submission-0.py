# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        # reverse second list
        prev = None
        curr = head2

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        head2 = prev
        start = head

        while head2:
            next1 = head.next
            next2 = head2.next

            head.next = head2
            head2.next = next1

            head = next1
            head2 = next2
        
            

        
        
        